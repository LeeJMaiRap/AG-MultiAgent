import { redirect } from 'next/navigation';
import { getSession, verifyAdmin, createSession } from '@/lib/auth';

export default async function AdminLogin() {
  const session = await getSession();
  if (session) {
    redirect('/admin');
  }

  async function handleLogin(formData: FormData) {
    'use server';
    
    const username = formData.get('username') as string;
    const password = formData.get('password') as string;
    
    const admin = await verifyAdmin(username, password);
    
    if (admin) {
      await createSession(admin);
      redirect('/admin');
    } else {
      redirect('/admin/login?error=1');
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
      <div className="max-w-md w-full bg-white rounded-lg shadow-lg p-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-6 text-center">
          Đăng nhập quản trị
        </h1>
        
        <form action={handleLogin} className="space-y-6">
          <div>
            <label htmlFor="username" className="block text-sm font-medium text-gray-700 mb-2">
              Tên đăng nhập
            </label>
            <input
              type="text"
              id="username"
              name="username"
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
              Mật khẩu
            </label>
            <input
              type="password"
              id="password"
              name="password"
              required
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          
          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors font-medium"
          >
            Đăng nhập
          </button>
        </form>
        
        <div className="mt-4 text-center">
          <a href="/" className="text-sm text-gray-600 hover:text-gray-900">
            ← Quay lại trang chủ
          </a>
        </div>
      </div>
    </div>
  );
}
