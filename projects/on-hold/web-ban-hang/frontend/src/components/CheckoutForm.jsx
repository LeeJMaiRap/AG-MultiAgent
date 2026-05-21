import { useState } from 'react';
import { Link } from 'react-router-dom';
import { CreditCard, Banknote, Smartphone, ShieldCheck, Truck } from 'lucide-react';

const PAYMENT_METHODS = [
  { id: 'cod', label: 'Thanh toán khi nhận hàng', icon: <Truck size={20} />, description: 'Thanh toán trực tiếp khi nhận hàng' },
  { id: 'bank', label: 'Chuyển khoản ngân hàng', icon: <Banknote size={20} />, description: 'Chuyển khoản qua ngân hàng' },
  { id: 'card', label: 'Thẻ tín dụng/ghi nợ', icon: <CreditCard size={20} />, description: 'Visa, MasterCard, JCB' },
  { id: 'momo', label: 'Ví điện tử MoMo', icon: <Smartphone size={20} />, description: 'Thanh toán qua ứng dụng MoMo' },
];

const PROVINCES = [
  { value: 'hcm', label: 'TP. Hồ Chí Minh' },
  { value: 'hn', label: 'Hà Nội' },
  { value: 'hue', label: 'Thừa Thiên Huế' },
  { value: 'danang', label: 'Đà Nẵng' },
  { value: 'cantho', label: 'Cần Thơ' },
  { value: 'other', label: 'Tỉnh/Thành phố khác' },
];

function CheckoutForm({ cartItems, totalAmount, onPlaceOrder, onCancel }) {
  const [formData, setFormData] = useState({
    fullName: '',
    phone: '',
    email: '',
    address: '',
    province: '',
    ward: '',
    note: '',
  });
  const [paymentMethod, setPaymentMethod] = useState('cod');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errors, setErrors] = useState({});

  const handleChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    if (errors[field]) {
      setErrors(prev => {
        const newErrors = { ...prev };
        delete newErrors[field];
        return newErrors;
      });
    }
  };

  const validateForm = () => {
    const newErrors = {};
    
    if (!formData.fullName.trim()) {
      newErrors.fullName = 'Vui lòng nhập họ tên';
    }
    
    if (!formData.phone.trim()) {
      newErrors.phone = 'Vui lòng nhập số điện thoại';
    } else if (!/^[0-9+\s-]{10,15}$/.test(formData.phone)) {
      newErrors.phone = 'Số điện thoại không hợp lệ';
    }
    
    if (!formData.address.trim()) {
      newErrors.address = 'Vui lòng nhập địa chỉ';
    }
    
    if (!formData.province) {
      newErrors.province = 'Vui lòng chọn tỉnh/thành phố';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    setIsSubmitting(true);
    
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    onPlaceOrder({
      ...formData,
      paymentMethod,
      items: cartItems,
      total: totalAmount,
    });
    
    setIsSubmitting(false);
  };

  return (
    <div className="grid lg:grid-cols-3 gap-8">
      {/* Customer Info Form */}
      <div className="lg:col-span-2 space-y-6">
        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
          <h2 className="text-xl font-bold text-gray-900 mb-6 flex items-center gap-2">
            <ShieldCheck className="text-blue-600" size={24} />
            Thông tin giao hàng
          </h2>
          
          <form onSubmit={handleSubmit} className="space-y-5">
            <div className="grid md:grid-cols-2 gap-5">
              <div className="space-y-2">
                <label className="text-sm font-semibold text-gray-700">
                  Họ và tên <span className="text-red-500">*</span>
                </label>
                <input
                  type="text"
                  value={formData.fullName}
                  onChange={(e) => handleChange('fullName', e.target.value)}
                  placeholder="Nguyễn Văn A"
                  className={`w-full rounded-xl border ${errors.fullName ? 'border-red-500 bg-red-50' : 'border-gray-200'} px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all`}
                />
                {errors.fullName && (
                  <p className="text-red-500 text-xs">{errors.fullName}</p>
                )}
              </div>
              
              <div className="space-y-2">
                <label className="text-sm font-semibold text-gray-700">
                  Số điện thoại <span className="text-red-500">*</span>
                </label>
                <input
                  type="tel"
                  value={formData.phone}
                  onChange={(e) => handleChange('phone', e.target.value)}
                  placeholder="0901 234 567"
                  className={`w-full rounded-xl border ${errors.phone ? 'border-red-500 bg-red-50' : 'border-gray-200'} px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all`}
                />
                {errors.phone && (
                  <p className="text-red-500 text-xs">{errors.phone}</p>
                )}
              </div>
            </div>
            
            <div className="space-y-2">
              <label className="text-sm font-semibold text-gray-700">
                Email
              </label>
              <input
                type="email"
                value={formData.email}
                onChange={(e) => handleChange('email', e.target.value)}
                placeholder="example@email.com"
                className="w-full rounded-xl border border-gray-200 px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all"
              />
            </div>
            
            <div className="space-y-2">
              <label className="text-sm font-semibold text-gray-700">
                Địa chỉ giao hàng <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                value={formData.address}
                onChange={(e) => handleChange('address', e.target.value)}
                placeholder="Số nhà, tên đường, tổ/dân phố"
                className={`w-full rounded-xl border ${errors.address ? 'border-red-500 bg-red-50' : 'border-gray-200'} px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all`}
              />
              {errors.address && (
                <p className="text-red-500 text-xs">{errors.address}</p>
              )}
            </div>
            
            <div className="grid md:grid-cols-3 gap-5">
              <div className="space-y-2">
                <label className="text-sm font-semibold text-gray-700">
                  Tỉnh/Thành phố <span className="text-red-500">*</span>
                </label>
                <select
                  value={formData.province}
                  onChange={(e) => handleChange('province', e.target.value)}
                  className={`w-full rounded-xl border ${errors.province ? 'border-red-500 bg-red-50' : 'border-gray-200'} px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all`}
                >
                  <option value="">Chọn tỉnh/thành phố</option>
                  {PROVINCES.map(prov => (
                    <option key={prov.value} value={prov.value}>{prov.label}</option>
                  ))}
                </select>
                {errors.province && (
                  <p className="text-red-500 text-xs">{errors.province}</p>
                )}
              </div>
              
              <div className="space-y-2">
                <label className="text-sm font-semibold text-gray-700">
                  Quận/Huyện
                </label>
                <select className="w-full rounded-xl border border-gray-200 px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all">
                  <option value="">Chọn quận/huyện</option>
                </select>
              </div>
              
              <div className="space-y-2">
                <label className="text-sm font-semibold text-gray-700">
                  Phường/Xã
                </label>
                <select className="w-full rounded-xl border border-gray-200 px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all">
                  <option value="">Chọn phường/xã</option>
                </select>
              </div>
            </div>
            
            <div className="space-y-2">
              <label className="text-sm font-semibold text-gray-700">
                Ghi chú
              </label>
              <textarea
                value={formData.note}
                onChange={(e) => handleChange('note', e.target.value)}
                placeholder="Ví dụ: Giao trước cửa nhà, gọi trước khi giao..."
                rows={3}
                className="w-full rounded-xl border border-gray-200 px-4 py-3 outline-none focus:border-blue-500 focus:ring-2 focus:ring-blue-100 transition-all resize-none"
              />
            </div>
          </form>
        </div>
        
        {/* Payment Methods */}
        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
          <h2 className="text-xl font-bold text-gray-900 mb-6">
            Phương thức thanh toán
          </h2>
          
          <div className="grid md:grid-cols-2 gap-4">
            {PAYMENT_METHODS.map(method => (
              <div
                key={method.id}
                onClick={() => setPaymentMethod(method.id)}
                className={`cursor-pointer rounded-xl border-2 p-4 transition-all ${
                  paymentMethod === method.id
                    ? 'border-blue-600 bg-blue-50'
                    : 'border-gray-100 hover:border-blue-200'
                }`}
              >
                <div className="flex items-start gap-3">
                  <div className={`mt-1 p-2 rounded-lg ${
                    paymentMethod === method.id ? 'bg-blue-100 text-blue-600' : 'bg-gray-100 text-gray-600'
                  }`}>
                    {method.icon}
                  </div>
                  <div>
                    <h3 className={`font-semibold ${
                      paymentMethod === method.id ? 'text-blue-700' : 'text-gray-900'
                    }`}>
                      {method.label}
                    </h3>
                    <p className="text-sm text-gray-500 mt-1">
                      {method.description}
                    </p>
                  </div>
                  {paymentMethod === method.id && (
                    <div className="ml-auto mt-1">
                      <div className="w-5 h-5 rounded-full bg-blue-600 flex items-center justify-center">
                        <div className="w-2.5 h-2.5 rounded-full bg-white" />
                      </div>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
        
        {/* Action Buttons */}
        <div className="flex gap-4">
          <Link
            to="/cart"
            className="flex-1 px-6 py-4 rounded-xl border-2 border-gray-200 text-gray-700 font-semibold hover:bg-gray-50 transition-colors"
          >
            Quay lại giỏ hàng
          </Link>
          <button
            type="submit"
            onClick={handleSubmit}
            disabled={isSubmitting}
            className="flex-[2] px-6 py-4 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            {isSubmitting ? (
              <>
                <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                Đang xử lý...
              </>
            ) : (
              <>
                Đặt hàng ngay
                <ShieldCheck size={20} />
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}

export default CheckoutForm;
