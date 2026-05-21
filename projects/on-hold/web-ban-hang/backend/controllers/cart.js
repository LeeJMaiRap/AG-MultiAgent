const Cart = require('../models/Cart');
const Product = require('../models/Product');

/**
 * Lấy giỏ hàng của người dùng
 * GET /api/cart
 * Requires: JWT authentication
 */
const getCart = async (req, res) => {
  try {
    const userId = req.user._id;

    // Tìm giỏ hàng của user
    let cart = await Cart.findOne({ userId });

    // Nếu chưa có giỏ hàng, tạo mới
    if (!cart) {
      cart = await Cart.create({ userId, items: [] });
    }

    res.status(200).json({
      success: true,
      data: cart
    });
  } catch (error) {
    console.error('Get cart error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi lấy giỏ hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

/**
 * Thêm sản phẩm vào giỏ hàng
 * POST /api/cart
 * Body: { productId, quantity }
 * Requires: JWT authentication
 */
const addToCart = async (req, res) => {
  try {
    const userId = req.user._id;
    const { productId, quantity } = req.body;

    // Validate input
    if (!productId || !quantity) {
      return res.status(400).json({
        success: false,
        message: 'Vui lòng cung cấp productId và quantity'
      });
    }

    if (quantity < 1) {
      return res.status(400).json({
        success: false,
        message: 'Số lượng phải ít nhất 1'
      });
    }

    // Kiểm tra sản phẩm có tồn tại không
    const product = await Product.findById(productId);
    if (!product) {
      return res.status(404).json({
        success: false,
        message: 'Sản phẩm không tồn tại'
      });
    }

    // Kiểm tra số lượng tồn kho
    if (product.stock < quantity) {
      return res.status(400).json({
        success: false,
        message: `Số lượng tồn kho không đủ. Còn lại: ${product.stock}`
      });
    }

    // Tìm hoặc tạo giỏ hàng
    let cart = await Cart.findOne({ userId });
    if (!cart) {
      cart = await Cart.create({ userId, items: [] });
    }

    // Kiểm tra sản phẩm đã có trong giỏ chưa
    const existingItem = cart.items.find(item => item.productId.toString() === productId);

    if (existingItem) {
      // Cập nhật số lượng
      existingItem.quantity += quantity;
    } else {
      // Thêm sản phẩm mới
      cart.items.push({
        productId,
        productName: product.name,
        price: product.price,
        quantity
      });
    }

    await cart.save();

    res.status(200).json({
      success: true,
      message: 'Thêm sản phẩm vào giỏ hàng thành công',
      data: cart
    });
  } catch (error) {
    console.error('Add to cart error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi thêm sản phẩm vào giỏ hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

/**
 * Cập nhật số lượng sản phẩm trong giỏ hàng
 * PUT /api/cart/:productId
 * Body: { quantity }
 * Requires: JWT authentication
 */
const updateCartItem = async (req, res) => {
  try {
    const userId = req.user._id;
    const { productId } = req.params;
    const { quantity } = req.body;

    // Validate input
    if (!quantity) {
      return res.status(400).json({
        success: false,
        message: 'Vui lòng cung cấp quantity'
      });
    }

    if (quantity < 1) {
      return res.status(400).json({
        success: false,
        message: 'Số lượng phải ít nhất 1'
      });
    }

    // Tìm giỏ hàng
    const cart = await Cart.findOne({ userId });
    if (!cart) {
      return res.status(404).json({
        success: false,
        message: 'Giỏ hàng không tồn tại'
      });
    }

    // Tìm sản phẩm trong giỏ
    const item = cart.items.find(item => item.productId.toString() === productId);
    if (!item) {
      return res.status(404).json({
        success: false,
        message: 'Sản phẩm không có trong giỏ hàng'
      });
    }

    // Kiểm tra số lượng tồn kho
    const product = await Product.findById(productId);
    if (product.stock < quantity) {
      return res.status(400).json({
        success: false,
        message: `Số lượng tồn kho không đủ. Còn lại: ${product.stock}`
      });
    }

    // Cập nhật số lượng
    item.quantity = quantity;
    await cart.save();

    res.status(200).json({
      success: true,
      message: 'Cập nhật giỏ hàng thành công',
      data: cart
    });
  } catch (error) {
    console.error('Update cart item error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi cập nhật giỏ hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

/**
 * Xóa sản phẩm khỏi giỏ hàng
 * DELETE /api/cart/:productId
 * Requires: JWT authentication
 */
const removeFromCart = async (req, res) => {
  try {
    const userId = req.user._id;
    const { productId } = req.params;

    // Tìm giỏ hàng
    const cart = await Cart.findOne({ userId });
    if (!cart) {
      return res.status(404).json({
        success: false,
        message: 'Giỏ hàng không tồn tại'
      });
    }

    // Xóa sản phẩm khỏi giỏ
    const initialLength = cart.items.length;
    cart.items = cart.items.filter(item => item.productId.toString() !== productId);

    if (cart.items.length === initialLength) {
      return res.status(404).json({
        success: false,
        message: 'Sản phẩm không có trong giỏ hàng'
      });
    }

    await cart.save();

    res.status(200).json({
      success: true,
      message: 'Xóa sản phẩm khỏi giỏ hàng thành công',
      data: cart
    });
  } catch (error) {
    console.error('Remove from cart error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi xóa sản phẩm khỏi giỏ hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

module.exports = {
  getCart,
  addToCart,
  updateCartItem,
  removeFromCart
};
