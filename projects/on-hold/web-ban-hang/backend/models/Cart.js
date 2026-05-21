const mongoose = require('mongoose');

/**
 * Cart Schema
 * Lưu giỏ hàng của người dùng (chưa đặt hàng).
 */
const cartSchema = new mongoose.Schema(
  {
    // ID của người dùng sở hữu giỏ hàng
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      required: [true, 'User ID là bắt buộc'],
      unique: true,
    },

    // Danh sách các sản phẩm trong giỏ hàng
    items: {
      type: [
        {
          // ID sản phẩm
          productId: {
            type: mongoose.Schema.Types.ObjectId,
            required: true,
          },
          // Tên sản phẩm (lưu snapshot)
          productName: {
            type: String,
            required: true,
          },
          // Giá sản phẩm
          price: {
            type: Number,
            required: true,
            min: 0,
          },
          // Số lượng sản phẩm trong giỏ
          quantity: {
            type: Number,
            required: true,
            min: [1, 'Số lượng phải ít nhất 1'],
          },
        },
      ],
      default: [],
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model('Cart', cartSchema);
