import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import AuthForm from '../components/AuthForm';
import { authAPI } from '../services/api';

const Login = () => {
  const navigate = useNavigate();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async (formData) => {
    setLoading(true);
    setError('');

    try {
      await authAPI.login({
        email: formData.email,
        password: formData.password,
      });

      navigate('/');
    } catch (err) {
      console.error('Login error:', err);
      setError(err.message || 'Đã xảy ra lỗi. Vui lòng thử lại.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[calc(100vh-200px)] flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Đăng nhập
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Hoặc{' '}
            <Link to="/register" className="font-medium text-blue-600 hover:text-blue-500">
              tạo tài khoản mới
            </Link>
          </p>
        </div>

        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          {error && (
            <div className="mb-4 bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}

          <AuthForm type="login" onSubmit={handleLogin} />

          {loading && (
            <div className="mt-4 text-center text-sm text-gray-600">
              Đang đăng nhập...
            </div>
          )}

          <div className="mt-6">
            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-300" />
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-2 bg-white text-gray-500">Demo credentials</span>
              </div>
            </div>
            <div className="mt-3 text-center text-xs text-gray-500">
              <p>Email: user@example.com</p>
              <p>Password: password</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
