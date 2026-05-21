const express = require('express');
const router = express.Router();
const { getProducts, getProductById } = require('../controllers/products');

/**
 * GET /api/products
 * Lấy danh sách sản phẩm với hỗ trợ filter
 * Query params:
 *   - category: lọc theo danh mục
 *   - search: tìm kiếm theo tên hoặc mô tả
 *   - minPrice: giá tối thiểu
 *   - maxPrice: giá tối đa
 */
router.get('/', getProducts);

/**
 * GET /api/products/:id
 * Lấy chi tiết một sản phẩm
 */
router.get('/:id', getProductById);

module.exports = router;
