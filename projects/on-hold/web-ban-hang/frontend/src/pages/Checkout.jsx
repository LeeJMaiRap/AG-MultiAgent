import { useState } from 'react';
import { Link } from 'react-router-dom';
import { CheckCircle, Package, Truck, MapPin, Phone, Mail } from 'lucide-react';
import CheckoutForm from '../components/CheckoutForm';

// Mock cart data
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

function Checkout() {
  const [orderPlaced, setOrderPlaced] = useState(false);
  const [orderData, setOrderData] = useState(null);

  const cartItems = MOCK_CART_ITEMS;
  const totalItems = cartItems.reduce((sum, item) => sum + item.quantity, 0);
  const totalPrice = cartItems.reduce((sum, item) => sum + (item.price * item.quantity), 0);
  const shippingFee = totalPrice > 0 ? 30000 : 0;
  const finalTotal = totalPrice + shippingFee;

  const handlePlaceOrder = (data) => {
    setOrderData(data);
    setOrderPlaced(true);
  };

  const handleCancel = () => {
    window.location.href = '/cart';
  };

  if (orderPlaced && orderData) {
    return (
      <div className="bg-gray-50 min-h-screen py-8">
        <div className="container mx-auto px-4 max-w-2xl">
          {/* Success Message */}
          <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8 text-center mb-8">
            <div className="flex justify-center mb-6">
              <div className="relative">
                <div className="absolute inset-0 bg-green-100 rounded-full animate-pulse" />
                <CheckCircle className="text-green-600 relative" size={80} />
              </div>
            </div>
            
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              Đặt hàng thành công!
            </h1>
            <p className="text-gray-600 mb-6">
              Cảm ơn bạn đã mua sắm. Đơn hàng của bạn đã được tiếp nhận.
            </p>
            
            <div className="bg-blue-50 rounded-xl p-4 mb-8 text-left">
              <p className="text-sm text-gray-600 mb-2">
                <span className="font-semibold">Mã đơn hàng:</span>
              </p>
              <p className="text-2xl font-bold text-blue-600 font-mono">
                #ORD{Date.now().toString().slice(-8)}
              </p>
            </div>
          </div>

          {/* Order Summary */}
          <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 mb-8">
            <h2 className="text-xl font-bold text-gray-900 mb-6">
              Thông tin đơn hàng
            </h2>
            
            {/* Customer Info */}
            <div className="space-y-4 mb-6 pb-6 border-b border-gray-200">
              <div className="flex items-start gap-3">
                <MapPin className="text-blue-600 mt-1 flex-shrink-0" size={20} />
                <div>
                  <p className="text-sm text-gray-600">Địa chỉ giao hàng</p>
                  <p className="font-semibold text-gray-900">
                    {orderData.address}, {orderData.province}
                  </p>
                </div>
              </div>
              
              <div className="flex items-start gap-3">
                <Phone className="text-blue-600 mt-1 flex-shrink-0" size={20} />
                <div>
                  <p className="text-sm text-gray-600">Số điện thoại</p>
                  <p className="font-semibold text-gray-900">{orderData.phone}</p>
                </div>
              </div>
              
              {orderData.email && (
                <div className="flex items-start gap-3">
                  <Mail className="text-blue-600 mt-1 flex-shrink-0" size={20} />
                  <div>
                    <p className="text-sm text-gray-600">Email</p>
                    <p className="font-semibold text-gray-900">{orderData.email}</p>
                  </div>
                </div>
              )}
            </div>

            {/* Payment Method */}
            <div className="mb-6 pb-6 border-b border-gray-200">
              <p className="text-sm text-gray-600 mb-2">Phương thức thanh toán</p>
              <p className="font-semibold text-gray-900">
                {orderData.paymentMethod === 'cod' && 'Thanh toán khi nhận hàng'}
                {orderData.paymentMethod === 'bank' && 'Chuyển khoản ngân hàng'}
                {orderData.paymentMethod === 'card' && 'Thẻ tín dụng/ghi nợ'}
                {orderData.paymentMethod === 'momo' && 'Ví điện tử MoMo'}
              </p>
            </div>

            {/* Order Items */}
            <div className="mb-6">
              <h3 className="font-semibold text-gray-900 mb-4">Sản phẩm đã đặt</h3>
              <div className="space-y-3">
                {orderData.items.map(item => (
                  <div key={item.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                    <div className="flex items-center gap-3">
                      <img
                        src={item.image}
                        alt={item.name}
                        className="w-12 h-12 rounded-lg object-cover"
                      />
                      <div>
                        <p className="font-medium text-gray-900">{item.name}</p>
                        <p className="text-sm text-gray-500">x{item.quantity}</p>
                      </div>
                    </div>
                    <p className="font-semibold text-gray-900">
                      {(item.price * item.quantity).toLocaleString('vi-VN')}₫
                    </p>
                  </div>
                ))}
              </div>
            </div>

            {/* Total */}
            <div className="space-y-2 pt-4 border-t border-gray-200">
              <div className="flex justify-between text-gray-600">
                <span>Tạm tính</span>
                <span>{totalPrice.toLocaleString('vi-VN')}₫</span>
              </div>
              <div className="flex justify-between text-gray-600">
                <span>Phí vận chuyển</span>
                <span>{shippingFee.toLocaleString('vi-VN')}₫</span>
              </div>
              <div className="flex justify-between text-lg font-bold text-gray-900 pt-2">
                <span>Tổng cộng</span>
                <span className="text-blue-600">{finalTotal.toLocaleString('vi-VN')}₫</span>
              </div>
            </div>
          </div>

          {/* Next Steps */}
          <div className="bg-blue-50 rounded-2xl border border-blue-200 p-6 mb-8">
            <h3 className="font-bold text-gray-900 mb-4 flex items-center gap-2">
              <Truck className="text-blue-600" size={20} />
              Các bước tiếp theo
            </h3>
            <ol className="space-y-3 text-sm text-gray-700">
              <li className="flex gap-3">
                <span className="flex-shrink-0 w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-bold">1</span>
                <span>Chúng tôi sẽ xác nhận đơn hàng trong vòng 1 giờ</span>
              </li>
              <li className="flex gap-3">
                <span className="flex-shrink-0 w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-bold">2</span>
                <span>Sản phẩm sẽ được chuẩn bị và gửi đi trong 24 giờ</span>
              </li>
              <li className="flex gap-3">
                <span className="flex-shrink-0 w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-bold">3</span>
                <span>Bạn sẽ nhận được thông báo khi hàng được giao</span>
              </li>
            </ol>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-col sm:flex-row gap-4">
            <Link
              to="/products"
              className="flex-1 px-6 py-4 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-700 transition-colors text-center"
            >
              Tiếp tục mua sắm
            </Link>
            <Link
              to="/"
              className="flex-1 px-6 py-4 rounded-xl border-2 border-gray-200 text-gray-700 font-semibold hover:bg-gray-50 transition-colors text-center"
            >
              Về trang chủ
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-gray-50 min-h-screen py-8">
      <div className="container mx-auto px-4 max-w-7xl">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Thanh toán</h1>
          <p className="text-gray-600">Hoàn tất đơn hàng của bạn</p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          {/* Main Content */}
          <div className="lg:col-span-2">
            <CheckoutForm
              cartItems={cartItems}
              totalAmount={finalTotal}
              onPlaceOrder={handlePlaceOrder}
              onCancel={handleCancel}
            />
          </div>

          {/* Order Summary Sidebar */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6 sticky top-4">
              <h2 className="text-xl font-bold text-gray-900 mb-6 flex items-center gap-2">
                <Package size={24} className="text-blue-600" />
                Tóm tắt đơn hàng
              </h2>

              {/* Items List */}
              <div className="space-y-3 mb-6 pb-6 border-b border-gray-200 max-h-96 overflow-y-auto">
                {cartItems.map(item => (
                  <div key={item.id} className="flex items-start gap-3">
                    <img
                      src={item.image}
                      alt={item.name}
                      className="w-16 h-16 rounded-lg object-cover flex-shrink-0"
                    />
                    <div className="flex-1 min-w-0">
                      <p className="font-medium text-gray-900 line-clamp-2">
                        {item.name}
                      </p>
                      <p className="text-sm text-gray-500">x{item.quantity}</p>
                      <p className="font-semibold text-gray-900 mt-1">
                        {(item.price * item.quantity).toLocaleString('vi-VN')}₫
                      </p>
                    </div>
                  </div>
                ))}
              </div>

              {/* Pricing */}
              <div className="space-y-3 mb-6 pb-6 border-b border-gray-200">
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

              {/* Total */}
              <div className="flex justify-between text-lg font-bold text-gray-900 mb-6">
                <span>Tổng cộng</span>
                <span className="text-blue-600">
                  {finalTotal.toLocaleString('vi-VN')}₫
                </span>
              </div>

              {/* Info Box */}
              <div className="bg-green-50 rounded-xl border border-green-200 p-4">
                <p className="text-sm text-green-800">
                  <span className="font-semibold">✓ Miễn phí vận chuyển</span> cho đơn hàng từ 500.000₫
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Checkout;
