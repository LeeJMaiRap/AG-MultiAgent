import { useState, useMemo } from 'react';
import { Edit, Trash2, Plus, Search, Filter } from 'lucide-react';

const CATEGORY_META = {
  electronics: { label: 'Điện tử', emoji: '💻' },
  fashion: { label: 'Thời trang', emoji: '👕' },
  books: { label: 'Sách', emoji: '📚' },
  home: { label: 'Gia dụng', emoji: '🏠' },
  beauty: { label: 'Làm đẹp', emoji: '💄' },
  sports: { label: 'Thể thao', emoji: '🏃' },
};

const formatPrice = (price) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(price);

const generateMockProducts = () => {
  const categoryKeys = Object.keys(CATEGORY_META);
  return Array.from({ length: 50 }, (_, index) => {
    const id = index + 1;
    const category = categoryKeys[index % categoryKeys.length];
    const meta = CATEGORY_META[category];
    const baseName = meta.names ? meta.names[index % meta.names.length] : 'Sản phẩm';
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
      image: `https://picsum.photos/seed/product-${id}/200/200`,
      status: index % 5 === 0 ? 'inactive' : 'active',
      badge: index % 9 === 0 ? 'Bán chạy' : index % 7 === 0 ? 'Mới' : 'Ưu đãi',
    };
  });
};

const ALL_PRODUCTS = generateMockProducts();

export default function AdminProductList() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [products, setProducts] = useState(ALL_PRODUCTS);
  const [showAddModal, setShowAddModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(null);

  const filteredProducts = useMemo(() => {
    const keyword = searchTerm.trim().toLowerCase();
    return products.filter((product) => {
      const matchesSearch = !keyword || product.name.toLowerCase().includes(keyword);
      const matchesCategory = selectedCategory === 'all' || product.category === selectedCategory;
      return matchesSearch && matchesCategory;
    });
  }, [searchTerm, selectedCategory, products]);

  const handleDelete = (id) => {
    setProducts(products.filter(p => p.id !== id));
    setShowDeleteModal(null);
  };

  const handleAddProduct = (e) => {
    e.preventDefault();
    const form = e.target;
    const newProduct = {
      id: products.length + 1,
      name: form.name.value,
      category: form.category.value,
      price: parseInt(form.price.value),
      image: `https://picsum.photos/seed/product-${products.length + 1}/200/200`,
      status: 'active',
      badge: 'Mới',
      rating: 4.5,
      sold: 0,
    };
    setProducts([newProduct, ...products]);
    setShowAddModal(false);
    form.reset();
  };

  return (
    <div className="space-y-4">
      {/* Toolbar */}
      <div className="flex flex-col sm:flex-row gap-4 justify-between items-center bg-white p-4 rounded-2xl border border-gray-100 shadow-sm">
        <div className="flex gap-3 w-full sm:w-auto">
          <div className="relative flex-1 sm:w-64">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Tìm sản phẩm..."
              className="w-full pl-10 pr-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none"
            />
          </div>
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="px-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 outline-none"
          >
            <option value="all">Tất cả danh mục</option>
            {Object.entries(CATEGORY_META).map(([key, meta]) => (
              <option key={key} value={key}>{meta.label}</option>
            ))}
          </select>
        </div>
        <button
          onClick={() => setShowAddModal(true)}
          className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700 transition"
        >
          <Plus size={18} />
          Thêm sản phẩm
        </button>
      </div>

      {/* Product Table */}
      <div className="bg-white rounded-2xl border border-gray-100 shadow-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-4 text-left text-sm font-semibold text-gray-700">Sản phẩm</th>
                <th className="px-6 py-4 text-left text-sm font-semibold text-gray-700">Danh mục</th>
                <th className="px-6 py-4 text-left text-sm font-semibold text-gray-700">Giá</th>
                <th className="px-6 py-4 text-left text-sm font-semibold text-gray-700">Đã bán</th>
                <th className="px-6 py-4 text-left text-sm font-semibold text-gray-700">Trạng thái</th>
                <th className="px-6 py-4 text-right text-sm font-semibold text-gray-700">Hành động</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {filteredProducts.map((product) => (
                <tr key={product.id} className="hover:bg-gray-50 transition">
                  <td className="px-6 py-4">
                    <div className="flex items-center gap-3">
                      <img
                        src={product.image}
                        alt={product.name}
                        className="w-12 h-12 rounded-lg object-cover"
                      />
                      <div>
                        <p className="font-medium text-gray-900">{product.name}</p>
                        <p className="text-xs text-gray-500">ID: {product.id}</p>
                      </div>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <span className="inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-700">
                      {CATEGORY_META[product.category]?.emoji} {CATEGORY_META[product.category]?.label}
                    </span>
                  </td>
                  <td className="px-6 py-4 font-medium text-gray-900">
                    {formatPrice(product.price)}
                  </td>
                  <td className="px-6 py-4 text-gray-600">
                    {product.sold.toLocaleString('vi-VN')}
                  </td>
                  <td className="px-6 py-4">
                    <span className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium ${
                      product.status === 'active' 
                        ? 'bg-green-100 text-green-700' 
                        : 'bg-red-100 text-red-700'
                    }`}>
                      {product.status === 'active' ? 'Đang bán' : 'Ngừng bán'}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <div className="flex items-center justify-end gap-2">
                      <button className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition">
                        <Edit size={16} />
                      </button>
                      <button
                        onClick={() => setShowDeleteModal(product.id)}
                        className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition"
                      >
                        <Trash2 size={16} />
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {filteredProducts.length === 0 && (
          <div className="p-8 text-center text-gray-500">
            Không tìm thấy sản phẩm nào
          </div>
        )}

        {/* Pagination */}
        <div className="flex items-center justify-between px-6 py-4 border-t border-gray-100">
          <span className="text-sm text-gray-500">
            Hiển thị {filteredProducts.length} sản phẩm
          </span>
          <div className="flex gap-2">
            <button className="px-3 py-1 rounded-lg border border-gray-200 text-sm disabled:opacity-50" disabled>
              Trước
            </button>
            <button className="px-3 py-1 rounded-lg border border-gray-200 text-sm disabled:opacity-50" disabled>
              Sau
            </button>
          </div>
        </div>
      </div>

      {/* Add Product Modal */}
      {showAddModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-2xl w-full max-w-md p-6">
            <h3 className="text-lg font-bold mb-4">Thêm sản phẩm mới</h3>
            <form onSubmit={handleAddProduct} className="space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1">Tên sản phẩm</label>
                <input
                  name="name"
                  required
                  className="w-full px-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Danh mục</label>
                <select
                  name="category"
                  className="w-full px-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 outline-none"
                >
                  {Object.entries(CATEGORY_META).map(([key, meta]) => (
                    <option key={key} value={key}>{meta.label}</option>
                  ))}
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Giá</label>
                <input
                  name="price"
                  type="number"
                  required
                  min="0"
                  className="w-full px-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 outline-none"
                />
              </div>
              <div className="flex gap-3 mt-6">
                <button
                  type="button"
                  onClick={() => setShowAddModal(false)}
                  className="flex-1 px-4 py-2 rounded-xl border border-gray-200 hover:bg-gray-50"
                >
                  Hủy
                </button>
                <button
                  type="submit"
                  className="flex-1 px-4 py-2 rounded-xl bg-blue-600 text-white hover:bg-blue-700"
                >
                  Thêm
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Delete Confirmation Modal */}
      {showDeleteModal && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-2xl w-full max-w-md p-6">
            <h3 className="text-lg font-bold mb-2">Xác nhận xóa</h3>
            <p className="text-gray-600 mb-6">
              Bạn có chắc chắn muốn xóa sản phẩm này? Hành động này không thể hoàn tác.
            </p>
            <div className="flex gap-3">
              <button
                onClick={() => setShowDeleteModal(null)}
                className="flex-1 px-4 py-2 rounded-xl border border-gray-200 hover:bg-gray-50"
              >
                Hủy
              </button>
              <button
                onClick={() => handleDelete(showDeleteModal)}
                className="flex-1 px-4 py-2 rounded-xl bg-red-600 text-white hover:bg-red-700"
              >
                Xóa
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
