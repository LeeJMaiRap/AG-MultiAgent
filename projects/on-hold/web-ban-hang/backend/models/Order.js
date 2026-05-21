const mongoose = require('mongoose');

/**
 * Order Schema
 * Lưu thông tin đơn hàng của người dùng.
 */
const orderSchema = new mongoose.Schema(
  {
    // ID của người dùng đặt hàng
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      required: [true, 'User ID là bắt buộc'],
    },

    // Danh sách các sản phẩm trong đơn hàng
    items: {
      type: [
        {
          // ID sản phẩm
          productId: {
            type: mongoose.Schema.Types.ObjectId,
            required: true,
          },
          // Tên sản phẩm (lưu snapshot tại thời điểm đặt hàng)
          productName: {
            type: String,
            required: true,
          },
          // Giá sản phẩm tại thời điểm đặt hàng
          price: {
            type: Number,
            required: true,
            min: 0,
          },
          // Số lượng sản phẩm
          quantity: {
            type: Number,
            required: true,
            min: [1, 'Số lượng phải ít nhất 1'],
          },
        },
      ],
      required: [true, 'Danh sách sản phẩm là bắt buộc'],
      validate: {
        validator: (v) => v.length > 0,
        message: 'Đơn hàng phải có ít nhất 1 sản phẩm',
      },
    },

    // Tổng tiền đơn hàng
    totalAmount: {
      type: Number,
      required: [true, 'Tổng tiền là bắt buộc'],
      min: [0, 'Tổng tiền không được âm'],
    },

    // Địa chỉ giao hàng
    shippingAddress: {
      type: String,
      required: [true, 'Địa chỉ giao hàng là bắt buộc'],
      trim: true,
      minlength: [10, 'Địa chỉ phải có ít nhất 10 ký tự'],
      maxlength: [500, 'Địa chỉ không được vượt quá 500 ký tự'],
    },

    // Trạng thái đơn hàng
    status: {
      type: String,
      enum: {
        values: ['pending', 'confirmed', 'shipped', 'delivered', 'cancelled'],
        message: 'Trạng thái đơn hàng không hợp lệ',
      },
      default: 'pending',
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model('Order', orderSchema);
