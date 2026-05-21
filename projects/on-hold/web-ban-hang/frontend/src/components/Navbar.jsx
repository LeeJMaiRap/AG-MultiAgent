import { Link } from 'react-router-dom';
import { Menu, X } from 'lucide-react';
import { useState } from 'react';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const categories = [
    { name: 'Tất cả sản phẩm', path: '/products' },
    { name: 'Điện tử', path: '/products?category=electronics' },
    { name: 'Thời trang', path: '/products?category=fashion' },
    { name: 'Sách', path: '/products?category=books' },
  ];

  return (
    <nav className="bg-gray-50 border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-12">
          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-8">
            {categories.map((cat) => (
              <Link
                key={cat.path}
                to={cat.path}
                className="text-gray-700 hover:text-blue-600 transition font-medium text-sm"
              >
                {cat.name}
              </Link>
            ))}
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden"
            onClick={() => setIsOpen(!isOpen)}
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>

          {/* User Links */}
          <div className="hidden md:flex space-x-4">
            <Link to="/login" className="text-gray-700 hover:text-blue-600 text-sm">
              Đăng nhập
            </Link>
            <Link to="/register" className="text-gray-700 hover:text-blue-600 text-sm">
              Đăng ký
            </Link>
          </div>
        </div>

        {/* Mobile Menu */}
        {isOpen && (
          <div className="md:hidden pb-4 space-y-2">
            {categories.map((cat) => (
              <Link
                key={cat.path}
                to={cat.path}
                className="block text-gray-700 hover:text-blue-600 py-2"
                onClick={() => setIsOpen(false)}
              >
                {cat.name}
              </Link>
            ))}
          </div>
        )}
      </div>
    </nav>
  );
}
