import { getDb } from '@/lib/db';
import Link from 'next/link';

interface Account {
  id: number;
  game: string;
  title: string;
  description: string;
  price: number;
  status: string;
}

export default async function Home({
  searchParams,
}: {
  searchParams: Promise<{ game?: string; search?: string }>;
}) {
  const params = await searchParams;
  const db = getDb();
  
  let query = 'SELECT * FROM accs WHERE status = ?';
  const queryParams: any[] = ['available'];
  
  if (params.game) {
    query += ' AND game = ?';
    queryParams.push(params.game);
  }
  
  if (params.search) {
    query += ' AND (title LIKE ? OR description LIKE ?)';
    const searchTerm = `%${params.search}%`;
    queryParams.push(searchTerm, searchTerm);
  }
  
  query += ' ORDER BY created_at DESC';
  
  const accounts = db.prepare(query).all(...queryParams) as Account[];
  
  // Get unique games for filter
  const games = db.prepare('SELECT DISTINCT game FROM accs ORDER BY game').all() as { game: string }[];

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center">
            <h1 className="text-3xl font-bold text-gray-900">Chợ Tài Khoản Game</h1>
            <Link 
              href="/admin/login"
              className="text-sm text-gray-600 hover:text-gray-900"
            >
              Quản trị
            </Link>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        {/* Filters */}
        <div className="bg-white rounded-lg shadow p-6 mb-8">
          <form method="get" className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1">
              <label htmlFor="search" className="block text-sm font-medium text-gray-700 mb-2">
                Tìm kiếm
              </label>
              <input
                type="text"
                id="search"
                name="search"
                defaultValue={params.search}
                placeholder="Nhập từ khóa..."
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
            </div>
            <div className="flex-1">
              <label htmlFor="game" className="block text-sm font-medium text-gray-700 mb-2">
                Game
              </label>
              <select
                id="game"
                name="game"
                defaultValue={params.game || ''}
                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="">Tất cả game</option>
                {games.map((g) => (
                  <option key={g.game} value={g.game}>
                    {g.game}
                  </option>
                ))}
              </select>
            </div>
            <div className="flex items-end">
              <button
                type="submit"
                className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
              >
                Lọc
              </button>
            </div>
          </form>
        </div>

        {/* Accounts Grid */}
        {accounts.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg">Không tìm thấy tài khoản nào</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {accounts.map((acc) => (
              <Link
                key={acc.id}
                href={`/acc/${acc.id}`}
                className="bg-white rounded-lg shadow hover:shadow-lg transition-shadow overflow-hidden"
              >
                <div className="p-6">
                  <div className="text-sm text-blue-600 font-medium mb-2">{acc.game}</div>
                  <h3 className="text-lg font-semibold text-gray-900 mb-2">{acc.title}</h3>
                  <p className="text-gray-600 text-sm mb-4 line-clamp-2">{acc.description}</p>
                  <div className="flex justify-between items-center">
                    <span className="text-2xl font-bold text-red-600">
                      {acc.price.toLocaleString('vi-VN')}đ
                    </span>
                    <span className="text-sm text-green-600 font-medium">Còn hàng</span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        )}
      </main>

      <footer className="bg-white border-t mt-12">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <p className="text-center text-gray-500 text-sm">
            © 2026 Chợ Tài Khoản Game. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
  );
}
