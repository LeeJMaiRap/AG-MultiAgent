const mongoose = require('mongoose');

/**
 * Database Connection Module
 * 
 * Kết nối MongoDB sử dụng mongoose
 * 
 * Cách sử dụng:
 * 1. Thêm MONGO_URI vào file .env
 * 2. Import và gọi connectDB() trong server.js:
 *    const connectDB = require('./config/database');
 *    connectDB();
 */

const connectDB = async () => {
  try {
    // Kiểm tra MONGO_URI có tồn tại không
    if (!process.env.MONGO_URI) {
      throw new Error('MONGO_URI is not defined in environment variables');
    }

    // Kết nối MongoDB
    const conn = await mongoose.connect(process.env.MONGO_URI, {
      // Các options này đã deprecated trong mongoose 6+, không cần nữa
      // useNewUrlParser: true,
      // useUnifiedTopology: true,
    });

    console.log(`✅ MongoDB Connected: ${conn.connection.host}`);
    console.log(`📦 Database: ${conn.connection.name}`);

    // Lắng nghe các events
    mongoose.connection.on('error', (err) => {
      console.error('❌ MongoDB connection error:', err);
    });

    mongoose.connection.on('disconnected', () => {
      console.warn('⚠️  MongoDB disconnected');
    });

    // Graceful shutdown
    process.on('SIGINT', async () => {
      await mongoose.connection.close();
      console.log('MongoDB connection closed through app termination');
      process.exit(0);
    });

  } catch (error) {
    console.error('❌ MongoDB connection failed:', error.message);
    
    // Log chi tiết hơn trong development mode
    if (process.env.NODE_ENV === 'development') {
      console.error('Error details:', error);
    }
    
    // Exit process nếu không kết nối được database
    process.exit(1);
  }
};

module.exports = connectDB;
