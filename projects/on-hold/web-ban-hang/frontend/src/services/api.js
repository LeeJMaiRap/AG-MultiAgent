/**
 * API Service - Kết nối với backend
 * Base URL: http://localhost:5000/api
 */

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

// Helper function để handle API responses
const handleResponse = async (response) => {
  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message || `API Error: ${response.status}`);
  }

  return data;
};

// Helper function để get auth token
const getAuthToken = () => {
  return localStorage.getItem('authToken');
};

// Helper function để set auth headers
const getHeaders = (includeAuth = false) => {
  const headers = {
    'Content-Type': 'application/json',
  };

  if (includeAuth) {
    const token = getAuthToken();
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }
  }

  return headers;
};

/**
 * PRODUCTS API
 */
export const productsAPI = {
  /**
   * Lấy danh sách sản phẩm
   * @param {Object} params - { category, search, minPrice, maxPrice }
   */
  getAll: async (params = {}) => {
    try {
      const queryString = new URLSearchParams(params).toString();
      const url = `${API_BASE_URL}/products${queryString ? `?${queryString}` : ''}`;

      const response = await fetch(url, {
        method: 'GET',
        headers: getHeaders(),
      });

      return await handleResponse(response);
    } catch (error) {
      console.error('Error fetching products:', error);
      throw error;
    }
  },

  /**
   * Lấy chi tiết sản phẩm theo ID
   * @param {string} id - Product ID
   */
  getById: async (id) => {
    try {
      const response = await fetch(`${API_BASE_URL}/products/${id}`, {
        method: 'GET',
        headers: getHeaders(),
      });

      return await handleResponse(response);
    } catch (error) {
      console.error(`Error fetching product ${id}:`, error);
      throw error;
    }
  },
};

/**
 * AUTH API
 */
export const authAPI = {
  /**
   * Đăng ký tài khoản mới
   * @param {Object} data - { name, email, password }
   */
  register: async (data) => {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/register`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify(data),
      });

      const result = await handleResponse(response);

      // Lưu token nếu đăng ký thành công
      if (result.data?.token) {
        localStorage.setItem('authToken', result.data.token);
        localStorage.setItem('user', JSON.stringify(result.data.user));
      }

      return result;
    } catch (error) {
      console.error('Error registering:', error);
      throw error;
    }
  },

  /**
   * Đăng nhập
   * @param {Object} data - { email, password }
   */
  login: async (data) => {
    try {
      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: 'POST',
        headers: getHeaders(),
        body: JSON.stringify(data),
      });

      const result = await handleResponse(response);

      // Lưu token nếu đăng nhập thành công
      if (result.data?.token) {
        localStorage.setItem('authToken', result.data.token);
        localStorage.setItem('user', JSON.stringify(result.data.user));
      }

      return result;
    } catch (error) {
      console.error('Error logging in:', error);
      throw error;
    }
  },

  /**
   * Đăng xuất
   */
  logout: () => {
    localStorage.removeItem('authToken');
    localStorage.removeItem('user');
  },

  /**
   * Lấy thông tin user hiện tại
   */
  getCurrentUser: () => {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
  },

  /**
   * Kiểm tra xem user đã đăng nhập chưa
   */
  isAuthenticated: () => {
    return !!getAuthToken();
  },
};

export default {
  productsAPI,
  authAPI,
};
