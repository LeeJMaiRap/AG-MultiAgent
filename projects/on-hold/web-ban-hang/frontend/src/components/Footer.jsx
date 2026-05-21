import { Globe, Send, Camera, Mail, Phone, MapPin } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-300 mt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
          {/* About */}
          <div>
            <h3 className="text-white font-bold text-lg mb-4">ShopHub</h3>
            <p className="text-sm">
              Nền tảng mua sắm trực tuyến hàng đầu với hàng triệu sản phẩm chất lượng.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-white font-bold mb-4">Liên kết nhanh</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white transition">Về chúng tôi</a></li>
              <li><a href="#" className="hover:text-white transition">Chính sách bảo mật</a></li>
              <li><a href="#" className="hover:text-white transition">Điều khoản sử dụng</a></li>
              <li><a href="#" className="hover:text-white transition">Liên hệ</a></li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="text-white font-bold mb-4">Liên hệ</h4>
            <div className="space-y-3 text-sm">
              <div className="flex items-center gap-2">
                <Phone size={16} />
                <span>1900-1234</span>
              </div>
              <div className="flex items-center gap-2">
                <Mail size={16} />
                <span>support@shophub.com</span>
              </div>
              <div className="flex items-center gap-2">
                <MapPin size={16} />
                <span>Huế, Việt Nam</span>
              </div>
            </div>
          </div>

          {/* Social */}
          <div>
            <h4 className="text-white font-bold mb-4">Theo dõi</h4>
            <div className="flex space-x-4">
              <a href="#" className="hover:text-white transition">
                <Globe size={20} />
              </a>
              <a href="#" className="hover:text-white transition">
                <Send size={20} />
              </a>
              <a href="#" className="hover:text-white transition">
                <Camera size={20} />
              </a>
            </div>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-gray-700 pt-8">
          <p className="text-center text-sm">
            &copy; 2026 ShopHub. Tất cả quyền được bảo lưu.
          </p>
        </div>
      </div>
    </footer>
  );
}
