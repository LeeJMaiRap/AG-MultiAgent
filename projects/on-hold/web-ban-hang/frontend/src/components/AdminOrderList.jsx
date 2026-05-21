import { useState, useMemo } from 'react';
import { Eye, Search, Filter, Package, Truck, CheckCircle, XCircle } from 'lucide-react';

const ORDER_STATUS = {
  pending: { label: 'Chờ xử lý', color: 'bg-amber-100 text-amber-700', icon: Package },
  shipping: { label: 'Đang giao', color: 'bg-blue-100 text-blue-700', icon: Truck },
  completed: { label: 'Hoàn thành', color: 'bg-green-100 text-green-700', icon: CheckCircle },
  cancelled: { label: 'Đã hủy', color: 'bg-red-100 text-red-700', icon: XCircle },
};

const formatPrice = (price) =>
  new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  }).format(price);

const generateMockOrders = () => {
  const statuses = Object.keys(ORDER_STATUS);
  const customerNames = ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Phạm Thị D', 'Hoàng Văn E'];
  const products = ['Tai nghe Bluetooth', 'Áo khoác Urban', 'Đồng hồ thông minh', 'Balo laptop', 'Sách lập trình'];
  
  return Array.from({ length: 30 }, (_, index) => {
    const id = 1000 + index;
    const status = statuses[index % statuses.length];
    const total = 299000 + ((index * 187531) % 5500000);
    const itemCount = 1 + (index % 4);
    const customerName = customerNames[index % customerNames.length];
    const date = new Date(2026, 3, 1 + (index % 24));

    return {
      id,
      customerName,
      customerEmail: `user${index + 1}@example.com`,
      productSummary: products[index % products.length],
      itemCount,
      total,
      status,
      date: date.toLocaleDateString('vi-VN'),
      paymentMethod: index % 2 === 0 ? 'COD' : 'Chuyển khoản',
      address: `${10 + index} Nguyễn Huệ, Huế`,
    };
  });
};

const ALL_ORDERS = generateMockOrders();

export default function AdminOrderList() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedStatus, setSelectedStatus] = useState('all');
  const [orders, setOrders] = useState(ALL_ORDERS);
  const [selectedOrder, setSelectedOrder] = useState(null);

  const filteredOrders = useMemo(() => {
    const keyword = searchTerm.trim().toLowerCase();
    return orders.filter((order) => {
      const matchesSearch = 
        !keyword || 
        order.customerName.toLowerCase().includes(keyword) ||
        order.id.toString().includes(keyword);
      const matchesStatus = selectedStatus === 'all' || order.status === selectedStatus;
      return matchesSearch && matchesStatus;
    });
  }, [searchTerm, selectedStatus, orders]);

  const handleStatusChange = (orderId, newStatus) => {
    setOrders(orders.map(order => 
      order.id === orderId ? { ...order, status: newStatus } : order
    ));
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
              placeholder="Tìm đơn hàng..."
              className="w-full pl-10 pr-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-100 outline-none"
            />
          </div>
          <select
            value={selectedStatus}
            onChange={(e) => setSelectedStatus(e.target.value)}
            className="px-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 outline-none"
          >
            <option value="all">Tất cả trạng thái</option>
            {Object.entries(ORDER_STATUS).map(([key, status]) => (
              <option key={key} value={key}>{status.label}</option>
            ))}
          </select>
        </div>
        <div className="text-sm text-gray-500">
          Tổng: <span className="font-medium text-gray-900">{filteredOrders.length} đơn hàng</span>
        </div>
      </div>

      {/* Order Cards / Table */}
      <div className="space-y-4">
        {filteredOrders.map((order) => {
          const StatusIcon = ORDER_STATUS[order.status].icon;
          return (
            <div key={order.id} className="bg-white rounded-2xl border border-gray-100 shadow-sm p-4 md:p-6">
              <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                <div className="flex-1">
                  <div className="flex flex-wrap items-center gap-3 mb-3">
                    <h3 className="text-lg font-bold text-gray-900">#{order.id}</h3>
                    <span className={`inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-medium ${ORDER_STATUS[order.status].color}`}>
                      <StatusIcon size={14} />
                      {ORDER_STATUS[order.status].label}
                    </span>
                    <span className="text-sm text-gray-500">{order.date}</span>
                  </div>

                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div>
                      <p className="text-xs text-gray-500 uppercase tracking-wide">Khách hàng</p>
                      <p className="font-medium text-gray-900">{order.customerName}</p>
                      <p className="text-sm text-gray-500">{order.customerEmail}</p>
                    </div>
                    <div>
                      <p className="text-xs text-gray-500 uppercase tracking-wide">Sản phẩm</p>
                      <p className="font-medium text-gray-900">{order.productSummary}</p>
                      <p className="text-sm text-gray-500">{order.itemCount} sản phẩm</p>
                    </div>
                    <div>
                      <p className="text-xs text-gray-500 uppercase tracking-wide">Thanh toán</p>
                      <p className="font-medium text-gray-900">{formatPrice(order.total)}</p>
                      <p className="text-sm text-gray-500">{order.paymentMethod}</p>
                    </div>
                    <div>
                      <p className="text-xs text-gray-500 uppercase tracking-wide">Địa chỉ</p>
                      <p className="font-medium text-gray-900 text-sm">{order.address}</p>
                    </div>
                  </div>
                </div>

                <div className="flex flex-col sm:flex-row gap-3 lg:w-auto">
                  <select
                    value={order.status}
                    onChange={(e) => handleStatusChange(order.id, e.target.value)}
                    className="px-4 py-2 rounded-xl border border-gray-200 focus:border-blue-500 outline-none text-sm"
                  >
                    {Object.entries(ORDER_STATUS).map(([key, status]) => (
                      <option key={key} value={key}>{status.label}</option>
                    ))}
                  </select>
                  <button
                    onClick={() => setSelectedOrder(order)}
                    className="flex items-center justify-center gap-2 px-4 py-2 rounded-xl border border-gray-200 hover:border-blue-500 hover:text-blue-600 transition"
                  >
                    <Eye size={16} />
                    Chi tiết
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {filteredOrders.length === 0 && (
        <div className="bg-white rounded-2xl border border-gray-100 shadow-sm p-8 text-center text-gray-500">
          Không tìm thấy đơn hàng nào
        </div>
      )}

      {/* Order Detail Modal */}
      {selectedOrder && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-2xl w-full max-w-2xl p-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-center justify-between mb-6">
              <div>
                <h3 className="text-xl font-bold text-gray-900">Chi tiết đơn hàng #{selectedOrder.id}</h3>
                <p className="text-sm text-gray-500">Ngày đặt: {selectedOrder.date}</p>
              </div>
              <button
                onClick={() => setSelectedOrder(null)}
                className="p-2 hover:bg-gray-100 rounded-lg"
              >
                ×
              </button>
            </div>

            <div className="space-y-6">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="bg-gray-50 p-4 rounded-xl">
                  <h4 className="font-medium text-gray-900 mb-3">Thông tin khách hàng</h4>
                  <div className="space-y-2 text-sm">
                    <p><span className="text-gray-500">Tên:</span> {selectedOrder.customerName}</p>
                    <p><span className="text-gray-500">Email:</span> {selectedOrder.customerEmail}</p>
                    <p><span className="text-gray-500">Địa chỉ:</span> {selectedOrder.address}</p>
                  </div>
                </div>
                <div className="bg-gray-50 p-4 rounded-xl">
                  <h4 className="font-medium text-gray-900 mb-3">Thông tin đơn hàng</h4>
                  <div className="space-y-2 text-sm">
                    <p><span className="text-gray-500">Sản phẩm:</span> {selectedOrder.productSummary}</p>
                    <p><span className="text-gray-500">Số lượng:</span> {selectedOrder.itemCount}</p>
                    <p><span className="text-gray-500">Thanh toán:</span> {selectedOrder.paymentMethod}</p>
                  </div>
                </div>
              </div>

              <div className="border-t border-gray-100 pt-4">
                <div className="flex items-center justify-between text-lg font-bold">
                  <span>Tổng cộng</span>
                  <span className="text-blue-600">{formatPrice(selectedOrder.total)}</span>
                </div>
              </div>

              <div className="flex gap-3 pt-4">
                <button
                  onClick={() => setSelectedOrder(null)}
                  className="flex-1 px-4 py-2 rounded-xl border border-gray-200 hover:bg-gray-50"
                >
                  Đóng
                </button>
                <button className="flex-1 px-4 py-2 rounded-xl bg-blue-600 text-white hover:bg-blue-700">
                  Cập nhật đơn hàng
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
