import { useState } from 'react';
import { ShoppingCart, Heart, Share2, CheckCircle, Star } from 'lucide-react';

const formatPrice = (price) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(price);

export default function ProductDetailInfo({ product, onAddToCart }) {
  const [quantity, setQuantity] = useState(1);
  const [activeImage, setActiveImage] = useState(0);

  const handleQuantityChange = (newQuantity) => {
    if (newQuantity >= 1 && newQuantity <= 10) {
      setQuantity(newQuantity);
    }
  };

  const handleAddToCart = () => {
    onAddToCart({ ...product, quantity });
  };

  return (
    <div className="flex flex-col gap-6">
      {/* Giá và Badge */}
      <div className="flex flex-wrap items-center gap-3">
        <span className="rounded-full bg-emerald-100 px-4 py-1.5 text-sm font-semibold text-emerald-700">
          {product.badge}
        </span>
        <span className="rounded-full bg-blue-100 px-4 py-1.5 text-sm font-semibold text-blue-700">
          {product.rating.toFixed(1)} ★ ({product.sold.toLocaleString('vi-VN')} đã bán)
        </span>
      </div>

      <h1 className="text-2xl font-bold text-gray-900 sm:text-3xl md:text-4xl leading-tight">
        {product.name}
      </h1>

      {/* Giá */}
      <div className="flex items-baseline gap-4">
        <p className="text-4xl font-extrabold text-blue-600 sm:text-5xl">
          {formatPrice(product.price)}
        </p>
        {product.oldPrice && (
          <p className="text-xl text-gray-400 line-through">
            {formatPrice(product.oldPrice)}
          </p>
        )}
      </div>

      {/* Mô tả ngắn */}
      <p className="text-gray-600 leading-relaxed">
        {product.description}
      </p>

      {/* Chọn số lượng */}
      <div className="flex items-center gap-4 rounded-2xl border border-gray-200 bg-gray-50 p-4">
        <span className="text-sm font-semibold text-gray-700">Số lượng:</span>
        <div className="flex items-center gap-3">
          <button
            onClick={() => handleQuantityChange(quantity - 1)}
            disabled={quantity <= 1}
            className="flex h-10 w-10 items-center justify-center rounded-xl bg-white shadow-sm transition hover:bg-gray-100 disabled:cursor-not-allowed disabled:opacity-50"
          >
            <span className="text-xl font-bold text-gray-600">-</span>
          </button>
          <span className="w-12 text-center text-lg font-bold text-gray-900">
            {quantity}
          </span>
          <button
            onClick={() => handleQuantityChange(quantity + 1)}
            disabled={quantity >= 10}
            className="flex h-10 w-10 items-center justify-center rounded-xl bg-white shadow-sm transition hover:bg-gray-100 disabled:cursor-not-allowed disabled:opacity-50"
          >
            <span className="text-xl font-bold text-gray-600">+</span>
          </button>
        </div>
        <span className="ml-auto text-sm text-gray-500">
          {product.stock > 0 ? (
            <span className="flex items-center gap-1 text-emerald-600">
              <CheckCircle size={16} />
              {product.stock} sản phẩm có sẵn
            </span>
          ) : (
            <span className="text-red-500">Hết hàng</span>
          )}
        </span>
      </div>

      {/* Nút hành động */}
      <div className="flex flex-col gap-3 sm:flex-row">
        <button
          onClick={handleAddToCart}
          disabled={product.stock <= 0}
          className="flex-1 inline-flex items-center justify-center gap-2 rounded-2xl bg-blue-600 px-6 py-4 text-lg font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
        >
          <ShoppingCart size={24} />
          Thêm vào giỏ
        </button>
        <div className="flex gap-3">
          <button className="flex h-14 w-14 items-center justify-center rounded-2xl border border-gray-200 bg-white hover:bg-gray-50 transition">
            <Heart size={24} className="text-gray-600" />
          </button>
          <button className="flex h-14 w-14 items-center justify-center rounded-2xl border border-gray-200 bg-white hover:bg-gray-50 transition">
            <Share2 size={24} className="text-gray-600" />
          </button>
        </div>
      </div>

      {/* Thông tin thêm */}
      <div className="grid grid-cols-2 gap-4 pt-4">
        <div className="flex items-center gap-2 rounded-xl bg-gray-50 p-3">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-emerald-100 text-emerald-600">
            <CheckCircle size={18} />
          </div>
          <div>
            <p className="text-xs font-semibold text-gray-900">Chính hãng</p>
            <p className="text-xs text-gray-500">100% chính hãng</p>
          </div>
        </div>
        <div className="flex items-center gap-2 rounded-xl bg-gray-50 p-3">
          <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-100 text-blue-600">
            <Star size={18} />
          </div>
          <div>
            <p className="text-xs font-semibold text-gray-900">Đánh giá</p>
            <p className="text-xs text-gray-500">{product.rating.toFixed(1)}/5.0</p>
          </div>
        </div>
      </div>
    </div>
  );
}
