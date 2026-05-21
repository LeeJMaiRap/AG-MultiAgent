import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import AuthForm from '../components/AuthForm';
import { authAPI } from '../services/api';

const Register = () => {
  const navigate = useNavigate();
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRegister = async (formData) => {
    setLoading(true);
    setError('');

    try {
      await authAPI.register({
        name: formData.fullName,
        email: formData.email,
        password: formData.password,
      });

      navigate('/');
    } catch (err) {
      console.error('Register error:', err);
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
            Đăng ký tài khoản
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Hoặc{' '}
            <Link to="/login" className="font-medium text-blue-600 hover:text-blue-500">
              đăng nhập nếu đã có tài khoản
            </Link>
          </p>
        </div>

        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          {error && (
            <div className="mb-4 bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}

          <AuthForm type="register" onSubmit={handleRegister} />

          {loading && (
            <div className="mt-4 text-center text-sm text-gray-600">
              Đang tạo tài khoản...
            </div>
          )}

          <div className="mt-6 text-center text-xs text-gray-500">
            <p>Bằng việc đăng ký, bạn đồng ý với</p>
            <p className="mt-1">
              <a href="#" className="text-blue-600 hover:text-blue-500">Điều khoản dịch vụ</a>
              {' và '}
              <a href="#" className="text-blue-600 hover:text-blue-500">Chính sách bảo mật</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Register;
