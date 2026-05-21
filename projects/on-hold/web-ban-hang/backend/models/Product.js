const mongoose = require('mongoose');

/**
 * Product Schema
 * Lưu thông tin sản phẩm trong cửa hàng.
 */
const productSchema = new mongoose.Schema(
  {
    // Tên sản phẩm
    name: {
      type: String,
      required: [true, 'Tên sản phẩm là bắt buộc'],
      trim: true,
      minlength: [3, 'Tên sản phẩm phải có ít nhất 3 ký tự'],
      maxlength: [200, 'Tên sản phẩm không được vượt quá 200 ký tự'],
    },

    // Mô tả chi tiết sản phẩm
    description: {
      type: String,
      required: [true, 'Mô tả sản phẩm là bắt buộc'],
      trim: true,
      minlength: [10, 'Mô tả phải có ít nhất 10 ký tự'],
      maxlength: [2000, 'Mô tả không được vượt quá 2000 ký tự'],
    },

    // Giá sản phẩm (VNĐ)
    price: {
      type: Number,
      required: [true, 'Giá sản phẩm là bắt buộc'],
      min: [0, 'Giá sản phẩm không được âm'],
    },

    // Danh mục sản phẩm
    category: {
      type: String,
      required: [true, 'Danh mục sản phẩm là bắt buộc'],
      trim: true,
      enum: {
        values: ['electronics', 'fashion', 'food', 'books', 'home', 'sports', 'other'],
        message: 'Danh mục không hợp lệ',
      },
    },

    // URL hình ảnh sản phẩm
    image: {
      type: String,
      required: [true, 'Hình ảnh sản phẩm là bắt buộc'],
      trim: true,
    },

    // Số lượng tồn kho
    stock: {
      type: Number,
      required: [true, 'Số lượng tồn kho là bắt buộc'],
      min: [0, 'Số lượng tồn kho không được âm'],
      default: 0,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model('Product', productSchema);
