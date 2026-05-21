import Database from 'better-sqlite3';
import bcrypt from 'bcryptjs';
import path from 'path';
import fs from 'fs';

const dataDir = path.join(process.cwd(), 'data');
const dbPath = path.join(dataDir, 'app.db');

// Ensure data directory exists
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

const db = new Database(dbPath);
db.pragma('journal_mode = WAL');

// Create tables
db.exec(`
  CREATE TABLE IF NOT EXISTS admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

  CREATE TABLE IF NOT EXISTS accs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    contact_phone TEXT NOT NULL,
    contact_facebook TEXT NOT NULL,
    image_url TEXT,
    status TEXT DEFAULT 'available',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

  CREATE INDEX IF NOT EXISTS idx_accs_game ON accs(game);
  CREATE INDEX IF NOT EXISTS idx_accs_status ON accs(status);
`);

// Seed admin
const adminPassword = bcrypt.hashSync('admin123', 10);
const insertAdmin = db.prepare(`
  INSERT OR IGNORE INTO admins (username, password_hash) VALUES (?, ?)
`);
insertAdmin.run('admin', adminPassword);

// Seed sample accounts (only if empty)
const existingAccs = db.prepare('SELECT COUNT(*) as count FROM accs').get() as { count: number };

if (existingAccs.count === 0) {
  const insertAcc = db.prepare(`
    INSERT INTO accs (game, title, description, price, contact_phone, contact_facebook, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `);

  const sampleAccs = [
  {
    game: 'Kingdom Story: Brave Legion',
    title: 'Tài khoản VIP 10 - Full tướng SSR',
    description: 'Tài khoản đã chơi 6 tháng, có đầy đủ tướng SSR mạnh, trang bị +15, nhiều tài nguyên.',
    price: 1500000,
    contact_phone: '0705460062',
    contact_facebook: 'https://www.facebook.com/doanhnt.274',
    status: 'available'
  },
  {
    game: 'Kingdom Story: Brave Legion',
    title: 'Acc mới VIP 5 - Giá rẻ',
    description: 'Tài khoản mới chơi 1 tháng, VIP 5, có một số tướng SSR tốt để phát triển.',
    price: 500000,
    contact_phone: '0705460062',
    contact_facebook: 'https://www.facebook.com/doanhnt.274',
    status: 'available'
  },
  {
    game: 'Liên Minh Huyền Thoại',
    title: 'Acc Vàng 2 - 50 tướng 30 skin',
    description: 'Tài khoản rank Vàng 2, có 50 tướng và 30 skin đẹp, chưa bị phạt.',
    price: 800000,
    contact_phone: '0705460062',
    contact_facebook: 'https://www.facebook.com/doanhnt.274',
    status: 'available'
  },
  {
    game: 'Liên Minh Huyền Thoại',
    title: 'Acc Kim Cương 4 - Full skin hiếm',
    description: 'Tài khoản rank Kim Cương 4, có hơn 100 skin bao gồm nhiều skin giới hạn và hiếm.',
    price: 3000000,
    contact_phone: '0705460062',
    contact_facebook: 'https://www.facebook.com/doanhnt.274',
    status: 'available'
  },
  {
    game: 'PUBG',
    title: 'Acc PUBG Mobile - Conqueror mùa 20',
    description: 'Tài khoản đạt rank Conqueror mùa 20, có nhiều outfit và skin súng đẹp.',
    price: 2000000,
    contact_phone: '0705460062',
    contact_facebook: 'https://www.facebook.com/doanhnt.274',
    status: 'available'
  },
  {
    game: 'PUBG',
    title: 'Acc PUBG PC - Level cao nhiều skin',
    description: 'Tài khoản PUBG PC level 150+, có nhiều skin quần áo và vũ khí từ các season trước.',
    price: 1200000,
    contact_phone: '0705460062',
    contact_facebook: 'https://www.facebook.com/doanhnt.274',
    status: 'available'
  }
];

  for (const acc of sampleAccs) {
    insertAcc.run(
      acc.game,
      acc.title,
      acc.description,
      acc.price,
      acc.contact_phone,
      acc.contact_facebook,
      acc.status
    );
  }

  console.log(`📦 Seeded ${sampleAccs.length} sample accounts`);
} else {
  console.log(`📦 Accounts already exist: ${existingAccs.count}`);
}

console.log('✅ Database initialized successfully!');
console.log(`📁 Database location: ${dbPath}`);
console.log('👤 Admin user: admin / admin123');

db.close();
