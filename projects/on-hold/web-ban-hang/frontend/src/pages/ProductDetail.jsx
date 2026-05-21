import { useState, useMemo, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { ChevronLeft, Star, MessageCircle } from 'lucide-react';
import ProductDetailInfo from '../components/ProductDetailInfo';
import { productsAPI } from '../services/api';

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

const formatPrice = (price) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(price);

const generateProductById = (id) => {
  const categoryKeys = Object.keys(CATEGORY_META);
  const index = parseInt(id) - 1;
  const category = categoryKeys[index % categoryKeys.length];
  const meta = CATEGORY_META[category] || CATEGORY_META.other;
  const baseName = meta.names[index % meta.names.length];
  const variant = ((index * 7) % 48) + 1;
  const price = 89000 + ((index * 137531) % 5500000);
  const oldPrice = price + Math.floor(price * 0.2);
  const rating = (((index * 3) % 15) + 35) / 10;

  return {
    id: parseInt(id),
    name: `${baseName} ${meta.label} ${variant}`,
    category,
    price,
    oldPrice,
    rating,
    sold: 50 + ((index * 19) % 4000),
    stock: 15 + ((index * 11) % 50),
    image: `https://picsum.photos/seed/product-${id}/800/600`,
    images: [
      `https://picsum.photos/seed/product-${id}/800/600`,
      `https://picsum.photos/seed/product-${id}-2/800/600`,
      `https://picsum.photos/seed/product-${id}-3/800/600`,
      `https://picsum.photos/seed/product-${id}-4/800/600`,
    ],
    badge: index % 9 === 0 ? 'Bán chạy' : index % 7 === 0 ? 'Mới' : 'Ưu đãi',
    description: `Thiết kế hiện đại, chất lượng tốt, phù hợp cho nhu cầu hằng ngày và sử dụng lâu dài. Sản phẩm được kiểm tra kỹ lưỡng trước khi gửi đến tay khách hàng.`,
    fullDescription: `Đây là một sản phẩm chất lượng cao được tuyển chọn từ các nhà cung cấp uy tín. Sản phẩm có thiết kế hiện đại, bền bỉ và phù hợp với nhiều nhu cầu sử dụng khác nhau.

Đặc điểm nổi bật:
• Thiết kế đẹp mắt, hiện đại
• Chất lượng vật liệu tốt
• Bảo hành 12 tháng
• Giao hàng nhanh toàn quốc
• Hỗ trợ khách hàng 24/7

Sản phẩm này đã được hàng nghìn khách hàng tin tưởng và sử dụng. Hãy đặt hàng ngay để nhận được ưu đãi đặc biệt!`,
    emoji: meta.emoji,
    color: meta.color,
  };
};

const reviews = [
  {
    id: 1,
    author: 'Nguyễn Văn A',
    rating: 5,
    date: '2 ngày trước',
    content: 'Sản phẩm rất tốt, giao hàng nhanh, đóng gói cẩn thận. Rất hài lòng!',
    helpful: 24,
  },
  {
    id: 2,
    author: 'Trần Thị B',
    rating: 4,
    date: '1 tuần trước',
    content: 'Chất lượng ổn, giá hợp lý. Chỉ là giao hàng hơi lâu một chút.',
    helpful: 12,
  },
  {
    id: 3,
    author: 'Lê Minh C',
    rating: 5,
    date: '2 tuần trước',
    content: 'Tuyệt vời! Đúng như mô tả, sẽ mua lại lần nữa.',
    helpful: 18,
  },
];

function ReviewCard({ review }) {
  return (
    <div className="rounded-2xl border border-gray-200 bg-white p-5">
      <div className="mb-3 flex items-center justify-between">
        <div>
          <p className="font-semibold text-gray-900">{review.author}</p>
          <p className="text-sm text-gray-500">{review.date}</p>
        </div>
        <div className="flex gap-1">
          {Array.from({ length: 5 }).map((_, i) => (
            <Star
              key={i}
              size={16}
              className={i < review.rating ? 'fill-amber-400 text-amber-400' : 'text-gray-300'}
            />
          ))}
        </div>
      </div>
      <p className="mb-4 text-gray-700">{review.content}</p>
      <button className="flex items-center gap-2 text-sm text-gray-600 hover:text-blue-600 transition">
        <MessageCircle size={16} />
        Hữu ích ({review.helpful})
      </button>
    </div>
  );
}

export default function ProductDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [activeImageIndex, setActiveImageIndex] = useState(0);
  const [product, setProduct] = useState(() => generateProductById(id));
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProduct = async () => {
      setLoading(true);
      setError('');
      setActiveImageIndex(0);

      try {
        const response = await productsAPI.getById(id);
        if (response.success && response.data) {
          const p = response.data;
          const fallback = generateProductById(id);
          setProduct({
            id: p._id || p.id,
            name: p.name || fallback.name,
            category: p.category || fallback.category,
            price: p.price || fallback.price,
            oldPrice: p.oldPrice || fallback.oldPrice,
            rating: p.rating || fallback.rating,
            sold: p.sold || fallback.sold,
            stock: p.stock || fallback.stock,
            image: p.image || fallback.image,
            images: p.images?.length ? p.images : fallback.images,
            badge: p.badge || fallback.badge,
            description: p.description || fallback.description,
            fullDescription: p.fullDescription || p.description || fallback.fullDescription,
            emoji: CATEGORY_META[p.category]?.emoji || fallback.emoji,
            color: CATEGORY_META[p.category]?.color || fallback.color,
          });
        }
      } catch (err) {
        console.error('Error fetching product detail:', err);
        setError('Không thể tải chi tiết sản phẩm. Hiển thị dữ liệu mẫu.');
        setProduct(generateProductById(id));
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  const handleAddToCart = (cartItem) => {
    console.log('Thêm vào giỏ:', cartItem);
    alert(`Đã thêm ${cartItem.quantity} sản phẩm vào giỏ hàng!`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-slate-100">
      <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        {/* Nút quay lại */}
        <button
          onClick={() => navigate('/products')}
          className="mb-6 inline-flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-2.5 text-sm font-medium text-gray-700 transition hover:border-blue-500 hover:text-blue-600"
        >
          <ChevronLeft size={18} />
          Quay lại
        </button>

        {/* Breadcrumb */}
        <div className="mb-8 flex items-center gap-2 text-sm text-gray-600">
          <span>Trang chủ</span>
          <span>/</span>
          <span>Sản phẩm</span>
          <span>/</span>
          <span className="text-gray-900 font-semibold">{product.name}</span>
        </div>

        {error && (
          <div className="mb-6 rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-700">
            ⚠️ {error}
          </div>
        )}

        {loading ? (
          <div className="flex flex-col items-center justify-center rounded-3xl border border-gray-200 bg-white py-20 shadow-sm">
            <div className="mb-4 h-12 w-12 animate-spin rounded-full border-4 border-blue-200 border-t-blue-600"></div>
            <p className="text-sm text-gray-500">Đang tải chi tiết sản phẩm...</p>
          </div>
        ) : (
        /* Main Content */
        <>
        <div className="grid gap-8 lg:grid-cols-2">
          {/* Hình ảnh sản phẩm */}
          <div className="flex flex-col gap-4">
            {/* Ảnh lớn */}
            <div
              className={`relative h-96 sm:h-[500px] rounded-3xl overflow-hidden bg-gradient-to-br ${product.color} shadow-lg`}
            >
              <img
                src={product.images[activeImageIndex]}
                alt={product.name}
                className="h-full w-full object-cover mix-blend-multiply opacity-90"
              />
              <div className="absolute inset-0 flex items-center justify-center text-8xl">
                {product.emoji}
              </div>
              <span className="absolute left-4 top-4 rounded-full bg-white/90 px-4 py-2 text-sm font-semibold text-gray-800 shadow-sm">
                {product.badge}
              </span>
            </div>

            {/* Ảnh nhỏ */}
            <div className="flex gap-3 overflow-x-auto pb-2">
              {product.images.map((image, index) => (
                <button
                  key={index}
                  onClick={() => setActiveImageIndex(index)}
                  className={`h-20 w-20 flex-shrink-0 rounded-xl overflow-hidden border-2 transition ${
                    activeImageIndex === index
                      ? 'border-blue-600 shadow-md'
                      : 'border-gray-200 hover:border-gray-300'
                  }`}
                >
                  <img
                    src={image}
                    alt={`Ảnh ${index + 1}`}
                    className="h-full w-full object-cover"
                  />
                </button>
              ))}
            </div>
          </div>

          {/* Thông tin sản phẩm */}
          <ProductDetailInfo product={product} onAddToCart={handleAddToCart} />
        </div>

        {/* Mô tả chi tiết */}
        <div className="mt-12 rounded-3xl border border-gray-200 bg-white p-6 sm:p-8">
          <h2 className="mb-6 text-2xl font-bold text-gray-900">Mô tả chi tiết</h2>
          <div className="prose prose-sm max-w-none whitespace-pre-line leading-relaxed text-gray-700">
            {product.fullDescription}
          </div>
        </div>

        {/* Đánh giá */}
        <div className="mt-12">
          <div className="mb-8 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <h2 className="text-2xl font-bold text-gray-900">Đánh giá từ khách hàng</h2>
              <p className="mt-2 text-gray-600">
                {reviews.length} đánh giá | Trung bình {product.rating.toFixed(1)}/5.0 sao
              </p>
            </div>
            <button className="inline-flex items-center justify-center rounded-2xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700">
              Viết đánh giá
            </button>
          </div>

          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {reviews.map((review) => (
              <ReviewCard key={review.id} review={review} />
            ))}
          </div>
        </div>
        </>
        )}
      </div>
    </div>
  );
}
