const Order = require('../models/Order');
const Cart = require('../models/Cart');
const Product = require('../models/Product');

/**
 * Tạo đơn hàng từ giỏ hàng
 * POST /api/orders
 * Body: { shippingAddress }
 * Requires: JWT authentication
 */
const createOrder = async (req, res) => {
  try {
    const userId = req.user._id;
    const { shippingAddress } = req.body;

    // Validate input
    if (!shippingAddress) {
      return res.status(400).json({
        success: false,
        message: 'Vui lòng cung cấp địa chỉ giao hàng'
      });
    }

    if (shippingAddress.trim().length < 10) {
      return res.status(400).json({
        success: false,
        message: 'Địa chỉ giao hàng phải có ít nhất 10 ký tự'
      });
    }

    // Lấy giỏ hàng của user
    const cart = await Cart.findOne({ userId });
    if (!cart || cart.items.length === 0) {
      return res.status(400).json({
        success: false,
        message: 'Giỏ hàng trống, không thể tạo đơn hàng'
      });
    }

    // Tính tổng tiền và kiểm tra tồn kho
    let totalAmount = 0;
    const orderItems = [];

    for (const cartItem of cart.items) {
      const product = await Product.findById(cartItem.productId);

      if (!product) {
        return res.status(404).json({
          success: false,
          message: `Sản phẩm ${cartItem.productName} không tồn tại`
        });
      }

      if (product.stock < cartItem.quantity) {
        return res.status(400).json({
          success: false,
          message: `Sản phẩm ${cartItem.productName} không đủ số lượng. Còn lại: ${product.stock}`
        });
      }

      totalAmount += cartItem.price * cartItem.quantity;
      orderItems.push({
        productId: cartItem.productId,
        productName: cartItem.productName,
        price: cartItem.price,
        quantity: cartItem.quantity
      });
    }

    // Tạo đơn hàng
    const order = await Order.create({
      userId,
      items: orderItems,
      totalAmount,
      shippingAddress: shippingAddress.trim(),
      status: 'pending'
    });

    // Cập nhật tồn kho sản phẩm
    for (const item of orderItems) {
      await Product.findByIdAndUpdate(
        item.productId,
        { $inc: { stock: -item.quantity } }
      );
    }

    // Xóa giỏ hàng sau khi tạo đơn hàng
    await Cart.findOneAndUpdate({ userId }, { items: [] });

    res.status(201).json({
      success: true,
      message: 'Tạo đơn hàng thành công',
      data: order
    });
  } catch (error) {
    console.error('Create order error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi tạo đơn hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

/**
 * Lấy danh sách đơn hàng của người dùng
 * GET /api/orders
 * Requires: JWT authentication
 */
const getOrders = async (req, res) => {
  try {
    const userId = req.user._id;

    // Lấy tất cả đơn hàng của user
    const orders = await Order.find({ userId }).sort({ createdAt: -1 });

    res.status(200).json({
      success: true,
      count: orders.length,
      data: orders
    });
  } catch (error) {
    console.error('Get orders error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi lấy danh sách đơn hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

/**
 * Lấy chi tiết một đơn hàng
 * GET /api/orders/:id
 * Requires: JWT authentication
 */
const getOrderById = async (req, res) => {
  try {
    const userId = req.user._id;
    const { id } = req.params;

    // Validate MongoDB ObjectId
    if (!id.match(/^[0-9a-fA-F]{24}$/)) {
      return res.status(400).json({
        success: false,
        message: 'ID đơn hàng không hợp lệ'
      });
    }

    // Lấy đơn hàng
    const order = await Order.findById(id);

    if (!order) {
      return res.status(404).json({
        success: false,
        message: 'Đơn hàng không tồn tại'
      });
    }

    // Kiểm tra quyền: chỉ user sở hữu đơn hàng mới có thể xem
    if (order.userId.toString() !== userId.toString()) {
      return res.status(403).json({
        success: false,
        message: 'Bạn không có quyền xem đơn hàng này'
      });
    }

    res.status(200).json({
      success: true,
      data: order
    });
  } catch (error) {
    console.error('Get order by ID error:', error);
    res.status(500).json({
      success: false,
      message: 'Lỗi server khi lấy chi tiết đơn hàng',
      error: process.env.NODE_ENV === 'development' ? error.message : undefined
    });
  }
};

module.exports = {
  createOrder,
  getOrders,
  getOrderById
};
