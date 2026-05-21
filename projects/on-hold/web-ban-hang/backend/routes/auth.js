const express = require('express');
const router = express.Router();
const { register, login } = require('../controllers/auth');

/**
 * @route   POST /api/auth/register
 * @desc    Đăng ký user mới
 * @access  Public
 * @body    { name, email, password }
 */
router.post('/register', register);

/**
 * @route   POST /api/auth/login
 * @desc    Đăng nhập user
 * @access  Public
 * @body    { email, password }
 */
router.post('/login', login);

module.exports = router;
