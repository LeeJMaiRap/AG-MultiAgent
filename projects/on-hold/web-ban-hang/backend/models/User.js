const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

/**
 * User Schema
 * Lưu thông tin người dùng của hệ thống.
 */
const userSchema = new mongoose.Schema(
  {
    // Email dùng để đăng nhập, phải là duy nhất
    email: {
      type: String,
      required: [true, 'Email là bắt buộc'],
      unique: true,
      trim: true,
      lowercase: true,
      match: [/^\S+@\S+\.\S+$/, 'Email không hợp lệ'],
    },

    // Mật khẩu sẽ được hash trước khi lưu vào database
    password: {
      type: String,
      required: [true, 'Mật khẩu là bắt buộc'],
      minlength: [6, 'Mật khẩu phải có ít nhất 6 ký tự'],
    },

    // Tên hiển thị của người dùng
    name: {
      type: String,
      required: [true, 'Tên là bắt buộc'],
      trim: true,
      minlength: [2, 'Tên phải có ít nhất 2 ký tự'],
      maxlength: [100, 'Tên không được vượt quá 100 ký tự'],
    },

    // Vai trò người dùng trong hệ thống
    role: {
      type: String,
      enum: ['user', 'admin'],
      default: 'user',
    },
  },
  {
    timestamps: true,
  }
);

/**
 * Middleware hash mật khẩu trước khi lưu.
 * Chỉ hash khi password có thay đổi.
 */
userSchema.pre('save', async function (next) {
  if (!this.isModified('password')) {
    return next();
  }

  try {
    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

module.exports = mongoose.model('User', userSchema);
