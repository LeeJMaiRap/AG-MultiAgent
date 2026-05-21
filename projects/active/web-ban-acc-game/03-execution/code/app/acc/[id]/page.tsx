import { getDb } from '@/lib/db';
import Link from 'next/link';
import { notFound } from 'next/navigation';

interface Account {
  id: number;
  game: string;
  title: string;
  description: string;
  price: number;
  contact_phone: string;
  contact_facebook: string;
  status: string;
  created_at: string;
}

export default async function AccountDetail({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const db = getDb();
  
  const account = db.prepare('SELECT * FROM accs WHERE id = ?').get(id) as Account | undefined;
  
  if (!account) {
    notFound();
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <Link href="/" className="text-blue-600 hover:text-blue-800 text-sm font-medium">
            ← Quay lại trang chủ
          </Link>
        </div>
      </header>

      <main className="max-w-4xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="bg-white rounded-lg shadow-lg overflow-hidden">
          <div className="p-8">
            <div className="mb-4">
              <span className="inline-block px-3 py-1 bg-blue-100 text-blue-800 text-sm font-medium rounded-full">
                {account.game}
              </span>
            </div>
            
            <h1 className="text-3xl font-bold text-gray-900 mb-4">{account.title}</h1>
            
            <div className="mb-6">
              <span className="text-4xl font-bold text-red-600">
                {account.price.toLocaleString('vi-VN')}đ
              </span>
              <span className="ml-4 inline-block px-3 py-1 bg-green-100 text-green-800 text-sm font-medium rounded">
                {account.status === 'available' ? 'Còn hàng' : 'Đã bán'}
              </span>
            </div>

            <div className="border-t border-gray-200 pt-6 mb-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-3">Mô tả chi tiết</h2>
              <p className="text-gray-700 whitespace-pre-line leading-relaxed">
                {account.description}
              </p>
            </div>

            <div className="border-t border-gray-200 pt-6">
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Thông tin liên hệ</h2>
              <div className="space-y-3">
                <div className="flex items-center">
                  <span className="text-gray-600 font-medium w-32">Điện thoại:</span>
                  <a 
                    href={`tel:${account.contact_phone}`}
                    className="text-blue-600 hover:text-blue-800 font-medium"
                  >
                    {account.contact_phone}
                  </a>
                </div>
                <div className="flex items-center">
                  <span className="text-gray-600 font-medium w-32">Facebook:</span>
                  <a 
                    href={account.contact_facebook}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-600 hover:text-blue-800 font-medium"
                  >
                    {account.contact_facebook}
                  </a>
                </div>
              </div>
            </div>

            <div className="mt-8 flex gap-4">
              <a
                href={`tel:${account.contact_phone}`}
                className="flex-1 bg-green-600 text-white text-center py-3 px-6 rounded-lg font-semibold hover:bg-green-700 transition-colors"
              >
                Gọi ngay
              </a>
              <a
                href={account.contact_facebook}
                target="_blank"
                rel="noopener noreferrer"
                className="flex-1 bg-blue-600 text-white text-center py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition-colors"
              >
                Nhắn tin Facebook
              </a>
            </div>
          </div>
        </div>

        <div className="mt-6 text-center text-sm text-gray-500">
          Đăng ngày: {new Date(account.created_at).toLocaleDateString('vi-VN')}
        </div>
      </main>
    </div>
  );
}
