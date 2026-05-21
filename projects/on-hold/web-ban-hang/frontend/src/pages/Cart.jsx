import { useState } from 'react';
import { Link } from 'react-router-dom';
import { ShoppingCart, ArrowRight, Package } from 'lucide-react';
import CartItem from '../components/CartItem';

// Mock data
const MOCK_CART_ITEMS = [
  {
    id: 1,
    name: 'iPhone 15 Pro Max',
    category: 'Điện thoại',
    price: 29990000,
    quantity: 1,
    image: 'https://images.unsplash.com/photo-1696446702183-cbd50c6e8e0f?w=400&h=400&fit=crop'
  },
  {
    id: 2,
    name: 'MacBook Pro M3',
    category: 'Laptop',
    price: 45990000,
    quantity: 1,
    image: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400&h=400&fit=crop'
  },
  {
    id: 3,
    name: 'AirPods Pro 2',
    category: 'Phụ kiện',
    price: 6490000,
    quantity: 2,
    image: 'https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400&h=400&fit=crop'
  }
];

function Cart() {
  const [cartItems, setCartItems] = useState(MOCK_CART_ITEMS);

  const handleUpdateQuantity = (id, newQuantity) => {
    setCartItems(items =>
      items.map(item =>
        item.id === id ? { ...item, quantity: newQuantity } : item
      )
    );
  };

  const handleRemoveItem = (id) => {
    setCartItems(items => items.filter(item => item.id !== id));
  };

  const totalItems = cartItems.reduce((sum, item) => sum + item.quantity, 0);
  const totalPrice = cartItems.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  const shippingFee = totalPrice > 0 ? 30000 : 0;
  const finalTotal = totalPrice + shippingFee;

  return (
    <div className="bg-gray-50 min-h-screen py-8">
      <div className="container mx-auto px-4 max-w-6xl">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <ShoppingCart className="text-blue-600" size={32} />
          <h1 className="text-3xl font-bold text-gray-900">Giỏ hàng của bạn</h1>
          {totalItems > 0 && (
            <span className="bg-blue-600 text-white px-3 py-1 rounded-full text-sm font-semibold">
              {totalItems} sản phẩm
            </span>
          )}
        </div>

        {cartItems.length === 0 ? (
          /* Empty Cart */
          <div className="bg-white rounded-lg shadow-sm p-12 text-center">
            <Package className="mx-auto text-gray-300 mb-4" size={64} />
            <h2 className="text-2xl font-semibold text-gray-700 mb-2">
              Giỏ hàng trống
            </h2>
            <p className="text-gray-500 mb-6">
              Bạn chưa có sản phẩm nào trong giỏ hàng
            </p>
            <Link
              to="/products"
              className="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors font-semibold"
            >
              Tiếp tục mua sắm
              <ArrowRight size={20} />
            </Link>
          </div>
        ) : (
          /* Cart with Items */
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Cart Items */}
            <div className="lg:col-span-2 space-y-4">
              {cartItems.map(item => (
                <CartItem
                  key={item.id}
                  item={item}
                  onUpdateQuantity={handleUpdateQuantity}
                  onRemove={handleRemoveItem}
                />
              ))}
            </div>

            {/* Order Summary */}
            <div className="lg:col-span-1">
              <div className="bg-white rounded-lg shadow-sm p-6 sticky top-4">
                <h2 className="text-xl font-bold text-gray-900 mb-4">
                  Tóm tắt đơn hàng
                </h2>

                <div className="space-y-3 mb-4 pb-4 border-b border-gray-200">
                  <div className="flex justify-between text-gray-600">
                    <span>Tạm tính ({totalItems} sản phẩm)</span>
                    <span className="font-semibold">
                      {totalPrice.toLocaleString('vi-VN')}₫
                    </span>
                  </div>
                  <div className="flex justify-between text-gray-600">
                    <span>Phí vận chuyển</span>
                    <span className="font-semibold">
                      {shippingFee.toLocaleString('vi-VN')}₫
                    </span>
                  </div>
                </div>

                <div className="flex justify-between text-lg font-bold text-gray-900 mb-6">
                  <span>Tổng cộng</span>
                  <span className="text-blue-600">
                    {finalTotal.toLocaleString('vi-VN')}₫
                  </span>
                </div>

                <Link
                  to="/checkout"
                  className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors font-semibold flex items-center justify-center gap-2 mb-3"
                >
                  Thanh toán
                  <ArrowRight size={20} />
                </Link>

                <Link
                  to="/products"
                  className="block text-center text-blue-600 hover:text-blue-700 font-medium"
                >
                  Tiếp tục mua sắm
                </Link>

                {/* Promo Info */}
                <div className="mt-6 p-4 bg-blue-50 rounded-lg">
                  <p className="text-sm text-gray-700">
                    <span className="font-semibold">🎉 Miễn phí vận chuyển</span> cho đơn hàng từ 500.000₫
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Cart;
