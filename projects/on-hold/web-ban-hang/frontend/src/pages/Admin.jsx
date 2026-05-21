import { useState } from 'react';
import { Link, Routes, Route } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Package, 
  ShoppingBag, 
  Users, 
  Settings, 
  LogOut,
  Menu,
  X
} from 'lucide-react';
import AdminProductList from '../components/AdminProductList';
import AdminOrderList from '../components/AdminOrderList';

const mockStats = {
  totalProducts: 1200,
  totalOrders: 458,
  totalRevenue: 125000000,
  activeUsers: 892
};

const formatPrice = (price) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(price);

export default function Admin() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('dashboard');

  const navItems = [
    { id: 'dashboard', label: 'Tổng quan', icon: LayoutDashboard },
    { id: 'products', label: 'Sản phẩm', icon: Package },
    { id: 'orders', label: 'Đơn hàng', icon: ShoppingBag },
    { id: 'users', label: 'Người dùng', icon: Users },
    { id: 'settings', label: 'Cài đặt', icon: Settings },
  ];

  return (
    <div className="min-h-screen bg-slate-50">
      {/* Mobile Header */}
      <div className="md:hidden flex items-center justify-between bg-white border-b border-gray-200 p-4">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
            <span className="text-white font-bold">A</span>
          </div>
          <span className="font-bold text-gray-900">Admin</span>
        </div>
        <button 
          onClick={() => setSidebarOpen(!sidebarOpen)}
          className="p-2 text-gray-600"
        >
          {sidebarOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      <div className="flex">
        {/* Sidebar */}
        <aside className={`
          fixed inset-y-0 left-0 z-50 w-64 bg-white border-r border-gray-200 transform transition-transform duration-300 ease-in-out
          md:relative md:translate-x-0
          ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}
        `}>
          <div className="flex items-center gap-3 p-6 border-b border-gray-100">
            <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center">
              <span className="text-white font-bold text-xl">A</span>
            </div>
            <div>
              <h1 className="font-bold text-gray-900 text-lg">Admin Panel</h1>
              <p className="text-xs text-gray-500">ShopHub Management</p>
            </div>
          </div>

          <nav className="p-4 space-y-1">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => {
                  setActiveTab(item.id);
                  setSidebarOpen(false);
                }}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition ${
                  activeTab === item.id
                    ? 'bg-blue-50 text-blue-600 font-medium'
                    : 'text-gray-600 hover:bg-gray-50'
                }`}
              >
                <item.icon size={20} />
                {item.label}
              </button>
            ))}
          </nav>

          <div className="absolute bottom-0 left-0 right-0 p-4 border-t border-gray-100">
            <button className="w-full flex items-center gap-3 px-4 py-3 text-red-600 hover:bg-red-50 rounded-xl transition">
              <LogOut size={20} />
              Đăng xuất
            </button>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 md:ml-64">
          {/* Desktop Header */}
          <header className="hidden md:flex items-center justify-between p-6 border-b border-gray-200 bg-white">
            <div>
              <h2 className="text-xl font-bold text-gray-900">
                {navItems.find(n => n.id === activeTab)?.label}
              </h2>
              <p className="text-sm text-gray-500">Chào mừng trở lại, Admin!</p>
            </div>
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-2 px-4 py-2 bg-gray-50 rounded-lg">
                <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-medium">
                  AD
                </div>
                <div className="text-sm">
                  <p className="font-medium text-gray-900">Admin User</p>
                  <p className="text-gray-500 text-xs">admin@shophub.com</p>
                </div>
              </div>
            </div>
          </header>

          <div className="p-4 md:p-6">
            {activeTab === 'dashboard' && (
              <div className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                  {[
                    { label: 'Tổng sản phẩm', value: mockStats.totalProducts, icon: Package, color: 'bg-blue-500' },
                    { label: 'Tổng đơn hàng', value: mockStats.totalOrders, icon: ShoppingBag, color: 'bg-purple-500' },
                    { label: 'Doanh thu', value: formatPrice(mockStats.totalRevenue), icon: Users, color: 'bg-green-500' },
                    { label: 'Người dùng', value: mockStats.activeUsers, icon: Users, color: 'bg-orange-500' },
                  ].map((stat, idx) => (
                    <div key={idx} className="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-sm text-gray-500 mb-1">{stat.label}</p>
                          <p className="text-2xl font-bold text-gray-900">{stat.value}</p>
                        </div>
                        <div className={`w-12 h-12 ${stat.color} rounded-xl flex items-center justify-center text-white`}>
                          <stat.icon size={24} />
                        </div>
                      </div>
                    </div>
                  ))}
                </div>

                <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
                  <h3 className="text-lg font-bold text-gray-900 mb-4">Tình hình kinh doanh</h3>
                  <div className="h-64 flex items-end justify-between gap-2">
                    {[65, 72, 68, 85, 78, 92, 88, 95, 82, 76, 84, 90].map((h, i) => (
                      <div key={i} className="w-full bg-blue-50 rounded-t-lg relative group">
                        <div 
                          className="absolute bottom-0 left-0 right-0 bg-blue-500 rounded-t-lg transition-all duration-500 group-hover:bg-blue-600"
                          style={{ height: `${h}%` }}
                        />
                        <div className="absolute -bottom-6 left-1/2 -translate-x-1/2 text-xs text-gray-500">
                          {i + 1}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'products' && <AdminProductList />}
            {activeTab === 'orders' && <AdminOrderList />}
            
            {activeTab === 'users' && (
              <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8 text-center">
                <Users className="mx-auto text-gray-300 mb-4" size={48} />
                <h3 className="text-lg font-medium text-gray-900">Quản lý người dùng</h3>
                <p className="text-gray-500 mt-2">Chức năng đang phát triển</p>
              </div>
            )}

            {activeTab === 'settings' && (
              <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8 text-center">
                <Settings className="mx-auto text-gray-300 mb-4" size={48} />
                <h3 className="text-lg font-medium text-gray-900">Cài đặt hệ thống</h3>
                <p className="text-gray-500 mt-2">Chức năng đang phát triển</p>
              </div>
            )}
          </div>
        </main>
      </div>
    </div>
  );
}
