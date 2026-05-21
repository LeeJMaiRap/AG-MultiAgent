import { Trash2, Plus, Minus } from 'lucide-react';

function CartItem({ item, onUpdateQuantity, onRemove }) {
  const handleIncrease = () => {
    onUpdateQuantity(item.id, item.quantity + 1);
  };

  const handleDecrease = () => {
    if (item.quantity > 1) {
      onUpdateQuantity(item.id, item.quantity - 1);
    }
  };

  const subtotal = item.price * item.quantity;

  return (
    <div className="flex gap-4 p-4 bg-white rounded-lg shadow-sm border border-gray-200 hover:shadow-md transition-shadow">
      {/* Product Image */}
      <div className="w-24 h-24 flex-shrink-0">
        <img
          src={item.image}
          alt={item.name}
          className="w-full h-full object-cover rounded-md"
        />
      </div>

      {/* Product Info */}
      <div className="flex-1 min-w-0">
        <h3 className="font-semibold text-gray-900 truncate">{item.name}</h3>
        <p className="text-sm text-gray-500 mt-1">{item.category}</p>
        <p className="text-lg font-bold text-blue-600 mt-2">
          {item.price.toLocaleString('vi-VN')}₫
        </p>
      </div>

      {/* Quantity Controls */}
      <div className="flex flex-col items-end justify-between">
        <button
          onClick={() => onRemove(item.id)}
          className="text-red-500 hover:text-red-700 transition-colors"
          aria-label="Xóa sản phẩm"
        >
          <Trash2 size={20} />
        </button>

        <div className="flex items-center gap-2 border border-gray-300 rounded-lg">
          <button
            onClick={handleDecrease}
            className="p-2 hover:bg-gray-100 transition-colors rounded-l-lg"
            aria-label="Giảm số lượng"
          >
            <Minus size={16} />
          </button>
          <span className="px-3 font-semibold min-w-[2rem] text-center">
            {item.quantity}
          </span>
          <button
            onClick={handleIncrease}
            className="p-2 hover:bg-gray-100 transition-colors rounded-r-lg"
            aria-label="Tăng số lượng"
          >
            <Plus size={16} />
          </button>
        </div>

        <p className="text-lg font-bold text-gray-900">
          {subtotal.toLocaleString('vi-VN')}₫
        </p>
      </div>
    </div>
  );
}

export default CartItem;
