const express = require('express');
const router = express.Router();
const auth = require('../middleware/auth');
const { getCart, addToCart, updateCartItem, removeFromCart } = require('../controllers/cart');

/**
 * GET /api/cart
 * Lấy giỏ hàng của người dùng
 * Requires: JWT authentication
 */
router.get('/', auth, getCart);

/**
 * POST /api/cart
 * Thêm sản phẩm vào giỏ hàng
 * Body: { productId, quantity }
 * Requires: JWT authentication
 */
router.post('/', auth, addToCart);

/**
 * PUT /api/cart/:productId
 * Cập nhật số lượng sản phẩm trong giỏ hàng
 * Body: { quantity }
 * Requires: JWT authentication
 */
router.put('/:productId', auth, updateCartItem);

/**
 * DELETE /api/cart/:productId
 * Xóa sản phẩm khỏi giỏ hàng
 * Requires: JWT authentication
 */
router.delete('/:productId', auth, removeFromCart);

module.exports = router;
