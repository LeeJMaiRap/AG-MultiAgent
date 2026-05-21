import jwt from 'jsonwebtoken';
import bcrypt from 'bcryptjs';
import { cookies } from 'next/headers';
import { getDb } from './db';

const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-change-in-production';
const COOKIE_NAME = 'admin_token';

export interface AdminUser {
  id: number;
  username: string;
}

export async function verifyAdmin(username: string, password: string): Promise<AdminUser | null> {
  const db = getDb();
  const admin = db.prepare('SELECT * FROM admins WHERE username = ?').get(username) as any;
  
  if (!admin) return null;
  
  const isValid = bcrypt.compareSync(password, admin.password_hash);
  if (!isValid) return null;
  
  return { id: admin.id, username: admin.username };
}

export async function createSession(admin: AdminUser) {
  const token = jwt.sign({ id: admin.id, username: admin.username }, JWT_SECRET, {
    expiresIn: '7d'
  });
  
  const cookieStore = await cookies();
  cookieStore.set(COOKIE_NAME, token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    maxAge: 60 * 60 * 24 * 7 // 7 days
  });
}

export async function getSession(): Promise<AdminUser | null> {
  try {
    const cookieStore = await cookies();
    const token = cookieStore.get(COOKIE_NAME)?.value;
    
    if (!token) return null;
    
    const decoded = jwt.verify(token, JWT_SECRET) as AdminUser;
    return decoded;
  } catch {
    return null;
  }
}

export async function destroySession() {
  const cookieStore = await cookies();
  cookieStore.delete(COOKIE_NAME);
}
