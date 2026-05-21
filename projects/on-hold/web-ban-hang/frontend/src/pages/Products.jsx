import { useEffect, useMemo, useState } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { Eye, Filter, Search, ShoppingCart } from 'lucide-react';
import { productsAPI } from '../services/api';

const CATEGORY_OPTIONS = [
  { value: 'all', label: 'Tất cả' },
  { value: 'electronics', label: 'Điện tử' },
  { value: 'fashion', label: 'Thời trang' },
  { value: 'food', label: 'Thực phẩm' },
  { value: 'books', label: 'Sách' },
  { value: 'home', label: 'Gia dụng' },
  { value: 'sports', label: 'Thể thao' },
  { value: 'other', label: 'Khác' },
];

const CATEGORY_META = {
  electronics: {
    label: 'Điện tử',
    emoji: '💻',
    color: 'from-blue-500 to-cyan-400',
    names: ['Tai nghe', 'Chuột', 'Bàn phím', 'Màn hình', 'Loa Bluetooth', 'Webcam'],
  },
  fashion: {
    label: 'Thời trang',
    emoji: '👕',
    color: 'from-pink-500 to-rose-400',
    names: ['Áo thun', 'Áo khoác', 'Quần jean', 'Váy', 'Giày sneaker', 'Túi xách'],
  },
  food: {
    label: 'Thực phẩm',
    emoji: '🍎',
    color: 'from-orange-500 to-red-400',
    names: ['Trái cây', 'Bánh ngọt', 'Cà phê', 'Trà', 'Snack', 'Sữa hạt'],
  },
  books: {
    label: 'Sách',
    emoji: '📚',
    color: 'from-amber-500 to-orange-400',
    names: ['Sách kỹ năng', 'Tiểu thuyết', 'Sách lập trình', 'Sách kinh doanh', 'Manga', 'Sách thiếu nhi'],
  },
  home: {
    label: 'Gia dụng',
    emoji: '🏠',
    color: 'from-emerald-500 to-green-400',
    names: ['Nồi chiên', 'Máy xay', 'Đèn bàn', 'Kệ mini', 'Bình giữ nhiệt', 'Chăn ga'],
  },
  sports: {
    label: 'Thể thao',
    emoji: '🏃',
    color: 'from-lime-500 to-green-500',
    names: ['Thảm yoga', 'Áo thể thao', 'Bóng đá', 'Bình nước', 'Dây kháng lực', 'Giày chạy bộ'],
  },
  other: {
    label: 'Khác',
    emoji: '🎁',
    color: 'from-slate-500 to-gray-400',
    names: ['Phụ kiện', 'Quà tặng', 'Đồ tiện ích', 'Combo', 'Sản phẩm mới', 'Bộ sưu tập'],
  },
};

const PRODUCTS_PER_PAGE = 12;
const TOTAL_PRODUCTS = 1200;

const formatPrice = (price) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(price);

// Mock data fallback (sẽ bị override khi API thành công)
const generateMockProducts = () => {
  const categoryKeys = Object.keys(CATEGORY_META);

  return Array.from({ length: TOTAL_PRODUCTS }, (_, index) => {
    const id = index + 1;
    const category = categoryKeys[index % categoryKeys.length];
    const meta = CATEGORY_META[category];
    const baseName = meta.names[index % meta.names.length];
    const variant = ((index * 7) % 48) + 1;
    const price = 89000 + ((index * 137531) % 5500000);
    const rating = (((index * 3) % 15) + 35) / 10;

    return {
      id,
      name: `${baseName} ${meta.label} ${variant}`,
      category,
      price,
      rating,
      sold: 50 + ((index * 19) % 4000),
      image: `https://picsum.photos/seed/product-${id}/600/400`,
      badge: index % 9 === 0 ? 'Bán chạy' : index % 7 === 0 ? 'Mới' : 'Ưu đãi',
      description: `Thiết kế hiện đại, chất lượng tốt, phù hợp cho nhu cầu hằng ngày và sử dụng lâu dài.`,
      emoji: meta.emoji,
      color: meta.color,
    };
  });
};

const ALL_PRODUCTS = generateMockProducts();

function ProductCard({ product }) {
  return (
    <div className="group overflow-hidden rounded-2xl border border-gray-100 bg-white shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl">
      <div className={`relative h-52 bg-gradient-to-br ${product.color}`}>
        <img
          src={product.image}
          alt={product.name}
          className="h-full w-full object-cover mix-blend-multiply opacity-90 transition duration-300 group-hover:scale-105"
        />
        <div className="absolute inset-0 flex items-center justify-center text-6xl">
          {product.emoji}
        </div>
        <span className="absolute left-4 top-4 rounded-full bg-white/90 px-3 py-1 text-xs font-semibold text-gray-800 shadow-sm">
          {product.badge}
        </span>
      </div>

      <div className="p-5">
        <div className="mb-3 flex items-center justify-between gap-3">
          <span className="rounded-full bg-gray-100 px-3 py-1 text-xs font-medium text-gray-600">
            {CATEGORY_META[product.category]?.label || 'Khác'}
          </span>
          <span className="text-sm text-amber-500">★ {product.rating.toFixed(1)}</span>
        </div>

        <h3 className="mb-2 line-clamp-2 min-h-[56px] text-lg font-bold text-gray-900">
          {product.name}
        </h3>
        <p className="mb-4 line-clamp-2 text-sm text-gray-500">{product.description}</p>

        <div className="mb-4 flex items-end justify-between">
          <div>
            <p className="text-2xl font-extrabold text-blue-600">{formatPrice(product.price)}</p>
            <p className="text-sm text-gray-400">Đã bán {product.sold.toLocaleString('vi-VN')}</p>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-3">
          <Link
            to={`/products/${product.id}`}
            className="inline-flex items-center justify-center gap-2 rounded-xl border border-gray-200 px-4 py-2.5 text-sm font-medium text-gray-700 transition hover:border-blue-500 hover:text-blue-600"
          >
            <Eye size={16} />
            Xem chi tiết
          </Link>
          <button className="inline-flex items-center justify-center gap-2 rounded-xl bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white transition hover:bg-blue-700">
            <ShoppingCart size={16} />
            Thêm giỏ
          </button>
        </div>
      </div>
    </div>
  );
}

export default function Products() {
  const [showFilters, setShowFilters] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [currentPage, setCurrentPage] = useState(1);
  const [searchParams, setSearchParams] = useSearchParams();
  const [products, setProducts] = useState(ALL_PRODUCTS);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const categoryFromUrl = searchParams.get('category');
    const isValidCategory = categoryFromUrl && CATEGORY_OPTIONS.some((item) => item.value === categoryFromUrl);
    setSelectedCategory(isValidCategory ? categoryFromUrl : 'all');
    setCurrentPage(1);
  }, [searchParams]);

  // Fetch products from API when category or search changes
  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      setError('');

      try {
        const params = {};
        if (selectedCategory !== 'all') {
          params.category = selectedCategory;
        }
        if (searchTerm.trim()) {
          params.search = searchTerm.trim();
        }

        const response = await productsAPI.getAll(params);
        if (response.success && response.data) {
          // Map backend data to frontend format
          const mappedProducts = response.data.map((p) => ({
            id: p._id || p.id,
            name: p.name,
            category: p.category || 'electronics',
            price: p.price || 0,
            rating: p.rating || 0,
            sold: p.sold || 0,
            image: p.image || `https://picsum.photos/seed/product-${p._id || p.id}/600/400`,
            badge: p.badge || 'Ưu đãi',
            description: p.description || '',
            emoji: CATEGORY_META[p.category]?.emoji || '📦',
            color: CATEGORY_META[p.category]?.color || 'from-gray-500 to-gray-400',
          }));
          setProducts(mappedProducts);
        }
      } catch (err) {
        console.error('Error fetching products:', err);
        // Keep mock data as fallback
        setError('Không thể kết nối đến server. Hiển thị dữ liệu mẫu.');
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [selectedCategory, searchTerm]);

  const filteredProducts = useMemo(() => {
    const keyword = searchTerm.trim().toLowerCase();

    return products.filter((product) => {
      const matchesSearch = !keyword || product.name.toLowerCase().includes(keyword);
      const matchesCategory =
        selectedCategory === 'all' || product.category === selectedCategory;

      return matchesSearch && matchesCategory;
    });
  }, [products, searchTerm, selectedCategory]);

  const totalPages = Math.max(1, Math.ceil(filteredProducts.length / PRODUCTS_PER_PAGE));
  const currentProducts = filteredProducts.slice(
    (currentPage - 1) * PRODUCTS_PER_PAGE,
    currentPage * PRODUCTS_PER_PAGE
  );

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
    setCurrentPage(1);
  };

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setCurrentPage(1);

    if (category === 'all') {
      setSearchParams({});
      return;
    }

    setSearchParams({ category });
  };

  const paginationNumbers = useMemo(() => {
    const pages = [];
    const start = Math.max(1, currentPage - 2);
    const end = Math.min(totalPages, currentPage + 2);

    for (let page = start; page <= end; page += 1) {
      pages.push(page);
    }

    return pages;
  }, [currentPage, totalPages]);

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-slate-100">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-8 rounded-3xl bg-gradient-to-r from-blue-600 via-indigo-600 to-violet-600 p-6 text-white shadow-xl md:p-8">
          <p className="mb-2 text-sm font-medium uppercase tracking-[0.2em] text-blue-100">Kho sản phẩm</p>
          <h1 className="mb-3 text-3xl font-black md:text-4xl">Danh sách sản phẩm</h1>
          <p className="max-w-2xl text-sm text-blue-100 md:text-base">
            {loading ? 'Đang tải...' : `Khám phá hơn ${TOTAL_PRODUCTS.toLocaleString('vi-VN')} sản phẩm với giao diện hiện đại, hỗ trợ tìm kiếm, lọc danh mục và phân trang mượt mà.`}
          </p>
          {error && <p className="mt-2 text-sm text-blue-100">⚠️ {error}</p>}
        </div>

        <div className="flex flex-col gap-6 lg:flex-row">
          <aside className={`${showFilters ? 'block' : 'hidden'} lg:block lg:w-72`}>
            <div className="sticky top-6 rounded-3xl border border-gray-100 bg-white p-6 shadow-sm">
              <h2 className="mb-5 flex items-center gap-2 text-lg font-bold text-gray-900">
                <Filter size={20} className="text-blue-600" />
                Bộ lọc sản phẩm
              </h2>

              <div className="mb-6">
                <label className="mb-2 block text-sm font-semibold text-gray-700">Tìm kiếm theo tên</label>
                <div className="relative">
                  <Search size={18} className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                  <input
                    type="text"
                    value={searchTerm}
                    onChange={handleSearchChange}
                    placeholder="Ví dụ: Tai nghe, Áo thun..."
                    className="w-full rounded-2xl border border-gray-200 bg-gray-50 py-3 pl-10 pr-4 text-sm outline-none transition focus:border-blue-500 focus:bg-white"
                  />
                </div>
              </div>

              <div>
                <h3 className="mb-3 text-sm font-semibold text-gray-700">Danh mục</h3>
                <div className="space-y-2">
                  {CATEGORY_OPTIONS.map((category) => (
                    <button
                      key={category.value}
                      onClick={() => handleCategoryChange(category.value)}
                      className={`flex w-full items-center justify-between rounded-2xl px-4 py-3 text-left text-sm transition ${
                        selectedCategory === category.value
                          ? 'bg-blue-600 text-white shadow-md'
                          : 'bg-gray-50 text-gray-700 hover:bg-gray-100'
                      }`}
                    >
                      <span>{category.label}</span>
                      {selectedCategory === category.value && <span>✓</span>}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </aside>

          <section className="flex-1">
            <div className="mb-6 flex flex-col gap-4 rounded-3xl border border-gray-100 bg-white p-4 shadow-sm sm:flex-row sm:items-center sm:justify-between sm:p-5">
              <div className="flex flex-wrap items-center gap-3">
                <button
                  onClick={() => setShowFilters(!showFilters)}
                  className="inline-flex items-center gap-2 rounded-2xl border border-gray-200 px-4 py-2.5 text-sm font-medium text-gray-700 transition hover:border-blue-500 hover:text-blue-600 lg:hidden"
                >
                  <Filter size={18} />
                  Bộ lọc
                </button>
                <div>
                  <p className="text-sm text-gray-500">Kết quả hiển thị</p>
                  <p className="font-semibold text-gray-900">
                    {filteredProducts.length.toLocaleString('vi-VN')} sản phẩm
                  </p>
                </div>
              </div>

              <div className="text-sm text-gray-500">
                Trang <span className="font-semibold text-gray-900">{currentPage}</span> / {totalPages}
              </div>
            </div>

            {loading ? (
              <div className="flex flex-col items-center justify-center py-20">
                <div className="mb-4 h-12 w-12 animate-spin rounded-full border-4 border-blue-200 border-t-blue-600"></div>
                <p className="text-sm text-gray-500">Đang tải sản phẩm...</p>
              </div>
            ) : currentProducts.length > 0 ? (
              <>
                <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 xl:grid-cols-3">
                  {currentProducts.map((product) => (
                    <ProductCard key={product.id} product={product} />
                  ))}
                </div>

                <div className="mt-8 flex flex-wrap items-center justify-center gap-2">
                  <button
                    onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
                    disabled={currentPage === 1}
                    className="rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-gray-700 transition hover:border-blue-500 hover:text-blue-600 disabled:cursor-not-allowed disabled:opacity-50"
                  >
                    Trước
                  </button>

                  {paginationNumbers[0] > 1 && (
                    <>
                      <button
                        onClick={() => setCurrentPage(1)}
                        className="rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-gray-700"
                      >
                        1
                      </button>
                      {paginationNumbers[0] > 2 && <span className="px-2 text-gray-400">...</span>}
                    </>
                  )}

                  {paginationNumbers.map((page) => (
                    <button
                      key={page}
                      onClick={() => setCurrentPage(page)}
                      className={`rounded-xl px-4 py-2 text-sm font-semibold transition ${
                        currentPage === page
                          ? 'bg-blue-600 text-white shadow-md'
                          : 'border border-gray-200 bg-white text-gray-700 hover:border-blue-500 hover:text-blue-600'
                      }`}
                    >
                      {page}
                    </button>
                  ))}

                  {paginationNumbers[paginationNumbers.length - 1] < totalPages && (
                    <>
                      {paginationNumbers[paginationNumbers.length - 1] < totalPages - 1 && (
                        <span className="px-2 text-gray-400">...</span>
                      )}
                      <button
                        onClick={() => setCurrentPage(totalPages)}
                        className="rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-gray-700"
                      >
                        {totalPages}
                      </button>
                    </>
                  )}

                  <button
                    onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
                    disabled={currentPage === totalPages}
                    className="rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-gray-700 transition hover:border-blue-500 hover:text-blue-600 disabled:cursor-not-allowed disabled:opacity-50"
                  >
                    Sau
                  </button>
                </div>
              </>
            ) : (
              <div className="rounded-3xl border border-dashed border-gray-300 bg-white px-6 py-16 text-center shadow-sm">
                <div className="mb-3 text-5xl">🔎</div>
                <h3 className="mb-2 text-xl font-bold text-gray-900">Không tìm thấy sản phẩm phù hợp</h3>
                <p className="text-sm text-gray-500">
                  Hãy thử đổi từ khóa tìm kiếm hoặc chọn danh mục khác để xem thêm sản phẩm.
                </p>
              </div>
            )}
          </section>
        </div>
      </div>
    </div>
  );
}
