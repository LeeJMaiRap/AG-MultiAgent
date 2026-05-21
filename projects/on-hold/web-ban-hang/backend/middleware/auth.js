const jwt = require('jsonwebtoken');
const User = require('../models/User');

/**
 * Middleware xác thực JWT token.
 * Token được gửi qua header: Authorization: Bearer <token>
 */
const auth = async (req, res, next) => {
  try {
    const authHeader = req.header('Authorization');

    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({
        success: false,
        message: 'Không tìm thấy token xác thực'
      });
    }

    // Lấy token từ header Bearer
    const token = authHeader.replace('Bearer ', '').trim();

    if (!token) {
      return res.status(401).json({
        success: false,
        message: 'Token không hợp lệ'
      });
    }

    // Verify token bằng secret trong .env
    const decoded = jwt.verify(token, process.env.JWT_SECRET);

    // Tìm user tương ứng và bỏ password khỏi response object
    const user = await User.findById(decoded.id).select('-password');

    if (!user) {
      return res.status(401).json({
        success: false,
        message: 'Người dùng không tồn tại hoặc token không còn hợp lệ'
      });
    }

    // Gắn thông tin user vào request để route sau có thể sử dụng
    req.user = user;
    next();
  } catch (error) {
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        success: false,
        message: 'Token không hợp lệ'
      });
    }

    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        success: false,
        message: 'Token đã hết hạn'
      });
    }

    console.error('Auth middleware error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi xác thực người dùng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

module.exports = auth;
