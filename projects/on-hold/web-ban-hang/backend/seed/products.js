const mongoose = require('mongoose');
const Product = require('../models/Product');
require('dotenv').config();

/**
 * Seed Script - Tạo 1000+ sản phẩm mẫu
 * Chạy: node seed/products.js
 */

// Dữ liệu sản phẩm theo danh mục
const productTemplates = {
  electronics: [
    { name: 'Smartphone', desc: 'Điện thoại thông minh với màn hình AMOLED, pin 5000mAh, camera 108MP' },
    { name: 'Laptop', desc: 'Máy tính xách tay hiệu năng cao, bộ xử lý Intel Core i7, RAM 16GB' },
    { name: 'Tablet', desc: 'Máy tính bảng 10 inch, pin 8000mAh, hỗ trợ stylus' },
    { name: 'Smartwatch', desc: 'Đồng hồ thông minh theo dõi sức khỏe, GPS, chống nước' },
    { name: 'Tai nghe', desc: 'Tai nghe không dây, chống ồn chủ động, pin 30 giờ' },
    { name: 'Camera', desc: 'Máy ảnh kỹ thuật số, cảm biến 48MP, quay video 4K' },
    { name: 'Loa Bluetooth', desc: 'Loa di động, âm thanh stereo, pin 24 giờ' },
    { name: 'Sạc nhanh', desc: 'Bộ sạc nhanh 65W, hỗ trợ nhiều thiết bị' },
    { name: 'Pin dự phòng', desc: 'Pin sạc dự phòng 20000mAh, sạc nhanh 65W' },
    { name: 'Cáp USB-C', desc: 'Cáp USB-C chất lượng cao, hỗ trợ sạc nhanh' },
  ],
  fashion: [
    { name: 'Áo thun', desc: 'Áo thun cotton 100%, thoáng mát, nhiều màu sắc' },
    { name: 'Quần jeans', desc: 'Quần jeans nam/nữ, co giãn tốt, bền bỉ' },
    { name: 'Áo khoác', desc: 'Áo khoác chống nước, giữ ấm, thiết kế hiện đại' },
    { name: 'Giày thể thao', desc: 'Giày thể thao thoáng khí, đệm êm, phù hợp chạy bộ' },
    { name: 'Giày da', desc: 'Giày da cao cấp, phù hợp công sở' },
    { name: 'Túi xách', desc: 'Túi xách nữ, chất liệu da PU, nhiều ngăn' },
    { name: 'Mũ', desc: 'Mũ lưỡi trai, chống nắng, thoáng khí' },
    { name: 'Khăn quàng', desc: 'Khăn quàng cổ, chất liệu lụa, mềm mại' },
    { name: 'Đồng hồ', desc: 'Đồng hồ tay nam/nữ, dây da, mặt kính sapphire' },
    { name: 'Kính mát', desc: 'Kính mát UV400, thiết kế thời trang' },
  ],
  food: [
    { name: 'Cà phê', desc: 'Cà phê rang xay, hương vị đậm đà, 500g' },
    { name: 'Trà', desc: 'Trà oolong cao cấp, hương thơm tự nhiên' },
    { name: 'Mật ong', desc: 'Mật ong nguyên chất, không pha trộn, 500ml' },
    { name: 'Dầu ăn', desc: 'Dầu ăn nguyên chất, chiết xuất từ hạt' },
    { name: 'Nước tương', desc: 'Nước tương truyền thống, vị mặn đậm' },
    { name: 'Bánh quy', desc: 'Bánh quy bơ, giòn tan, hương vị tự nhiên' },
    { name: 'Chocolate', desc: 'Chocolate đen 70%, giàu chất chống oxy hóa' },
    { name: 'Kẹo', desc: 'Kẹo dẻo, nhiều hương vị, không chất bảo quản' },
    { name: 'Hạt điều', desc: 'Hạt điều rang muối, giàu dinh dưỡng' },
    { name: 'Nước ép', desc: 'Nước ép trái cây tự nhiên, không đường' },
  ],
  books: [
    { name: 'Tiểu thuyết', desc: 'Tiểu thuyết văn học, tác phẩm kinh điển' },
    { name: 'Sách kỹ năng', desc: 'Sách phát triển kỹ năng sống, tư duy' },
    { name: 'Sách kinh tế', desc: 'Sách về kinh tế, quản lý, kinh doanh' },
    { name: 'Sách lịch sử', desc: 'Sách lịch sử, tiểu sử nhân vật nổi tiếng' },
    { name: 'Sách khoa học', desc: 'Sách khoa học phổ thông, dễ hiểu' },
    { name: 'Truyện tranh', desc: 'Truyện tranh, manga, comic' },
    { name: 'Sách nấu ăn', desc: 'Sách công thức nấu ăn, hướng dẫn chi tiết' },
    { name: 'Sách tâm lý', desc: 'Sách tâm lý học, hiểu bản thân' },
    { name: 'Sách du lịch', desc: 'Sách hướng dẫn du lịch, bản đồ chi tiết' },
    { name: 'Sách trẻ em', desc: 'Sách tranh cho trẻ em, phát triển trí tưởng tượng' },
  ],
  home: [
    { name: 'Gối', desc: 'Gối ngủ, chất liệu cotton, thoáng khí' },
    { name: 'Chăn', desc: 'Chăn ấm, chất liệu lụa, nhẹ nhàng' },
    { name: 'Rèm cửa', desc: 'Rèm cửa chống nắng, cách âm' },
    { name: 'Thảm', desc: 'Thảm trải sàn, chất liệu cao cấp' },
    { name: 'Đèn', desc: 'Đèn LED tiết kiệm điện, ánh sáng ấm' },
    { name: 'Bàn', desc: 'Bàn làm việc, thiết kế hiện đại' },
    { name: 'Ghế', desc: 'Ghế ngồi, lưng tựa thoải mái' },
    { name: 'Tủ', desc: 'Tủ lưu trữ, nhiều ngăn, tiết kiệm không gian' },
    { name: 'Kệ sách', desc: 'Kệ sách gỗ, chịu lực tốt' },
    { name: 'Gương', desc: 'Gương treo tường, khung gỗ đẹp' },
  ],
  sports: [
    { name: 'Tạ', desc: 'Tạ tập luyện, nhiều trọng lượng' },
    { name: 'Thảm yoga', desc: 'Thảm yoga, chất liệu TPE, chống trượt' },
    { name: 'Vợt cầu lông', desc: 'Vợt cầu lông, khung nhôm, nhẹ nhàng' },
    { name: 'Bóng đá', desc: 'Bóng đá chính hãng, da PU' },
    { name: 'Bóng rổ', desc: 'Bóng rổ cao su, bền bỉ' },
    { name: 'Xe đạp', desc: 'Xe đạp địa hình, 21 tốc độ' },
    { name: 'Giày chạy bộ', desc: 'Giày chạy bộ, đệm khí, thoáng khí' },
    { name: 'Áo thể thao', desc: 'Áo thể thao, vải thấm hút mồ hôi' },
    { name: 'Quần thể thao', desc: 'Quần thể thao, co giãn tốt' },
    { name: 'Balo thể thao', desc: 'Balo thể thao, chống nước, nhiều ngăn' },
  ],
  other: [
    { name: 'Nước hoa', desc: 'Nước hoa nam/nữ, hương thơm lâu' },
    { name: 'Kem dưỡng', desc: 'Kem dưỡng da, dưỡng ẩm sâu' },
    { name: 'Dầu gội', desc: 'Dầu gội, làm sạch, nuôi dưỡng tóc' },
    { name: 'Xà phòng', desc: 'Xà phòng tắm, thơm mát, dịu nhẹ' },
    { name: 'Bàn chải', desc: 'Bàn chải đánh răng, lông mềm' },
    { name: 'Kem đánh răng', desc: 'Kem đánh răng, trắng sáng' },
    { name: 'Khăn tắm', desc: 'Khăn tắm cotton, mềm mại' },
    { name: 'Bộ chăm sóc', desc: 'Bộ chăm sóc da, 5 sản phẩm' },
    { name: 'Mặt nạ', desc: 'Mặt nạ dưỡng da, dưỡng ẩm' },
    { name: 'Toner', desc: 'Toner cân bằng da, làm sạch sâu' },
  ],
};

// Hàm tạo tên sản phẩm độc đáo
function generateProductName(template, index) {
  const variants = ['Pro', 'Plus', 'Max', 'Ultra', 'Elite', 'Premium', 'Standard', 'Lite', 'Deluxe', 'Classic'];
  const variant = variants[index % variants.length];
  return `${template.name} ${variant} ${Math.floor(index / variants.length) + 1}`;
}

// Hàm tạo mô tả sản phẩm
function generateDescription(template) {
  const additions = [
    ' Chất lượng cao, bền bỉ.',
    ' Giá cả hợp lý, chất lượng tốt.',
    ' Được yêu thích bởi khách hàng.',
    ' Sản phẩm bán chạy nhất.',
    ' Đáng mua, rất tiết kiệm.',
    ' Hàng chính hãng, bảo hành.',
    ' Giao hàng nhanh, miễn phí.',
    ' Hỗ trợ khách hàng 24/7.',
    ' Có nhiều lựa chọn màu sắc.',
    ' Phù hợp cho mọi lứa tuổi.',
  ];
  const addition = additions[Math.floor(Math.random() * additions.length)];
  return template.desc + addition;
}

// Hàm tạo giá sản phẩm
function generatePrice(category) {
  const priceRanges = {
    electronics: [500000, 50000000],
    fashion: [50000, 5000000],
    food: [10000, 500000],
    books: [20000, 500000],
    home: [50000, 10000000],
    sports: [50000, 5000000],
    other: [20000, 1000000],
  };

  const [min, max] = priceRanges[category] || [10000, 50000000];
  const price = Math.floor(Math.random() * (max - min + 1)) + min;
  // Làm tròn đến 1000 gần nhất
  return Math.round(price / 1000) * 1000;
}

// Hàm tạo URL hình ảnh placeholder
function generateImageUrl(category, index) {
  const categoryMap = {
    electronics: 'electronics',
    fashion: 'fashion',
    food: 'food',
    books: 'books',
    home: 'home',
    sports: 'sports',
    other: 'other',
  };

  const cat = categoryMap[category];
  const imageId = (index % 100) + 1;
  return `https://via.placeholder.com/300x300?text=${cat}+${imageId}`;
}

// Hàm tạo số lượng tồn kho
function generateStock() {
  return Math.floor(Math.random() * 500) + 10;
}

// Hàm chính - Seed dữ liệu
async function seedProducts() {
  try {
    // Kết nối MongoDB
    await mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/web-ban-hang', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });

    console.log('✓ Kết nối MongoDB thành công');

    // Xóa sản phẩm cũ
    await Product.deleteMany({});
    console.log('✓ Xóa sản phẩm cũ');

    // Tạo mảng sản phẩm
    const products = [];
    let productIndex = 0;

    for (const [category, templates] of Object.entries(productTemplates)) {
      // Mỗi danh mục tạo ~150 sản phẩm (7 danh mục × 150 = 1050 sản phẩm)
      const productsPerCategory = 150;

      for (let i = 0; i < productsPerCategory; i++) {
        const template = templates[i % templates.length];
        const product = {
          name: generateProductName(template, i),
          description: generateDescription(template),
          price: generatePrice(category),
          category: category,
          image: generateImageUrl(category, productIndex),
          stock: generateStock(),
        };

        products.push(product);
        productIndex++;
      }
    }

    // Lưu vào database
    const result = await Product.insertMany(products);
    console.log(`✓ Tạo thành công ${result.length} sản phẩm`);

    // Thống kê theo danh mục
    const stats = await Product.aggregate([
      {
        $group: {
          _id: '$category',
          count: { $sum: 1 },
          avgPrice: { $avg: '$price' },
          minPrice: { $min: '$price' },
          maxPrice: { $max: '$price' },
        },
      },
      { $sort: { _id: 1 } },
    ]);

    console.log('\n📊 Thống kê sản phẩm theo danh mục:');
    console.log('─'.repeat(80));
    stats.forEach((stat) => {
      console.log(
        `${stat._id.padEnd(15)} | Số lượng: ${stat.count.toString().padStart(4)} | ` +
          `Giá TB: ${Math.round(stat.avgPrice).toLocaleString('vi-VN')}đ | ` +
          `Min: ${stat.minPrice.toLocaleString('vi-VN')}đ | ` +
          `Max: ${stat.maxPrice.toLocaleString('vi-VN')}đ`
      );
    });

    const totalProducts = await Product.countDocuments();
    console.log('─'.repeat(80));
    console.log(`📦 Tổng cộng: ${totalProducts} sản phẩm`);

    await mongoose.connection.close();
    console.log('\n✓ Hoàn thành seed dữ liệu');
    process.exit(0);
  } catch (error) {
    console.error('❌ Lỗi:', error.message);
    process.exit(1);
  }
}

// Chạy seed
seedProducts();
