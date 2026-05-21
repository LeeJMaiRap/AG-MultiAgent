const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const { createOrder, getOrders, getOrderById } = require('../controllers/orders');

/**
 * POST /api/orders
 * Tạo đơn hàng từ giỏ hàng
 * Body: { shippingAddress }
 * Requires: JWT authentication
 */
router.post('/', auth, createOrder);

/**
 * GET /api/orders
 * Lấy danh sách đơn hàng của người dùng
 * Requires: JWT authentication
 */
router.get('/', auth, getOrders);

/**
 * GET /api/orders/:id
 * Lấy chi tiết một đơn hàng
 * Requires: JWT authentication
 */
router.get('/:id', auth, getOrderById);

module.exports = router;
