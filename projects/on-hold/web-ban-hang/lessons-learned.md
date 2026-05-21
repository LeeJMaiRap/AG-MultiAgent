# Lessons Learned - Web Bán Hàng Project

**Ngày:** 24/04/2026  
**Người viết:** Lệ (AI Agent)  
**Task:** TASK-015 - Testing & Final Polish

---

## 🎓 Bài học chính

### 1. **Query Parameters & URL State Sync**

**Vấn đề:** Navbar có link category với query params (`?category=electronics`), nhưng trang Products không đọc URL params, nên filter không sync.

**Giải pháp:** Dùng `useSearchParams()` từ react-router-dom để:
- Đọc query params từ URL
- Cập nhật state khi URL thay đổi
- Cập nhật URL khi user thay đổi filter

**Code pattern:**
```jsx
const [searchParams, setSearchParams] = useSearchParams();

useEffect(() => {
  const categoryFromUrl = searchParams.get('category');
  if (categoryFromUrl) setSelectedCategory(categoryFromUrl);
}, [searchParams]);

const handleCategoryChange = (category) => {
  setSelectedCategory(category);
  setSearchParams({ category });
};
```

**Bài học:** Luôn sync URL state với component state để user có thể bookmark/share link và quay lại đúng filter.

---

### 2. **SPA Navigation vs Full Page Reload**

**Vấn đề:** Dùng `<a href>` cho internal links gây full page reload, mất state, chậm hơn.

**Giải pháp:** Dùng `<Link>` từ react-router-dom cho tất cả internal navigation.

**So sánh:**
```jsx
// ❌ Sai - Full page reload
<a href="/products">Sản phẩm</a>

// ✅ Đúng - SPA navigation
<Link to="/products">Sản phẩm</Link>
```

**Bài học:** Trong SPA, luôn dùng router Link để giữ state và performance.

---

### 3. **Form Submission Flow**

**Vấn đề:** CheckoutForm có `onCancel` callback phức tạp, và nút submit nằm ngoài `<form>`.

**Giải pháp:** 
- Nút "Quay lại" dùng `<Link>` thay vì callback
- Nút submit nằm trong `<form>` với `type="submit"`
- Form validation trong `handleSubmit`

**Pattern tốt:**
```jsx
<form onSubmit={handleSubmit}>
  {/* form fields */}
  <button type="submit">Submit</button>
  <Link to="/back">Back</Link>
</form>
```

**Bài học:** Keep form logic simple - dùng native form submission và router Link cho navigation.

---

### 4. **Responsive Design Breakpoints**

**Observation:** Dự án dùng Tailwind breakpoints:
- `sm:` (640px) - Tablet
- `md:` (768px) - Tablet+
- `lg:` (1024px) - Desktop
- `xl:` (1280px) - Large desktop

**Pattern thường dùng:**
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">
  {/* 1 col mobile, 2 col tablet, 4 col desktop */}
</div>
```

**Bài học:** Luôn test trên 3 breakpoint: mobile, tablet, desktop. Dùng `hidden md:flex` để ẩn/hiện element.

---

### 5. **Mock Data Generation**

**Pattern tốt:** Dự án dùng hàm `generateMockProducts()` để tạo 1200 sản phẩm từ seed data:

```jsx
const generateMockProducts = () => {
  return Array.from({ length: 1200 }, (_, index) => {
    const category = categoryKeys[index % categoryKeys.length];
    const price = 89000 + ((index * 137531) % 5500000);
    return { id: index + 1, category, price, ... };
  });
};
```

**Lợi ích:**
- Deterministic (cùng index → cùng data)
- Scalable (dễ tăng số lượng)
- Không cần file JSON lớn

**Bài học:** Dùng seed-based generation cho mock data thay vì hardcode array.

---

### 6. **Component Composition**

**Observation:** Dự án tách components tốt:
- `Header`, `Navbar`, `Footer` - Layout
- `CartItem`, `ProductCard` - Reusable
- `CheckoutForm`, `AdminProductList` - Feature-specific

**Bài học:** Tách component khi:
- Dùng lại ở nhiều chỗ
- Logic phức tạp
- Dễ test riêng

---

### 7. **Error Handling & Validation**

**Pattern tốt trong CheckoutForm:**
```jsx
const validateForm = () => {
  const newErrors = {};
  if (!formData.fullName.trim()) {
    newErrors.fullName = 'Vui lòng nhập họ tên';
  }
  setErrors(newErrors);
  return Object.keys(newErrors).length === 0;
};

const handleSubmit = (e) => {
  e.preventDefault();
  if (!validateForm()) return;
  // submit logic
};
```

**Bài học:** Validate trước submit, hiển thị error message rõ ràng, clear error khi user sửa.

---

### 8. **Loading States**

**Pattern tốt:**
```jsx
<button disabled={isSubmitting}>
  {isSubmitting ? (
    <>
      <Spinner />
      Đang xử lý...
    </>
  ) : (
    'Submit'
  )}
</button>
```

**Bài học:** Luôn show loading state khi submit form để user biết request đang xử lý.

---

### 9. **Tailwind CSS Best Practices**

**Tốt:**
- Dùng `rounded-xl`, `rounded-2xl` cho consistent border radius
- Dùng `shadow-sm`, `shadow-md` cho consistent shadows
- Dùng `gap-4`, `gap-6` cho consistent spacing
- Dùng `text-sm`, `text-base`, `text-lg` cho consistent font sizes

**Tránh:**
- Hardcode colors - dùng Tailwind palette
- Inline styles - dùng class names
- Magic numbers - dùng Tailwind spacing scale

**Bài học:** Consistency trong design tokens (colors, spacing, shadows) tạo UI cohesive.

---

### 10. **Testing Checklist**

**Nên test:**
- ✅ Tất cả trang chính
- ✅ Navigation flow (click link, quay lại)
- ✅ Form submission (valid + invalid)
- ✅ Filter/Search functionality
- ✅ Responsive (mobile, tablet, desktop)
- ✅ Empty states
- ✅ Loading states
- ✅ Modal dialogs
- ✅ Browser console (không có error)

**Bài học:** Có checklist testing để không bỏ sót.

---

## 💡 Recommendations cho lần sau

1. **State Management:** Nếu app phức tạp hơn, xem xét dùng Context API hoặc Redux cho cart/auth state
2. **Persistence:** Dùng localStorage để persist cart khi reload page
3. **Backend Integration:** Thay mock data bằng API calls với error handling
4. **Testing:** Thêm unit tests (Vitest) và E2E tests (Cypress)
5. **Performance:** Thêm lazy loading cho images, code splitting cho routes
6. **Accessibility:** Thêm ARIA labels, keyboard navigation, screen reader support
7. **Analytics:** Track user behavior (page views, clicks, conversions)

---

## 📚 Resources

- React Router: https://reactrouter.com/
- Tailwind CSS: https://tailwindcss.com/
- Lucide Icons: https://lucide.dev/
- Vite: https://vitejs.dev/

---

## ✨ Kết luận

Dự án này là một ví dụ tốt về:
- ✅ Clean component structure
- ✅ Responsive design
- ✅ Form handling
- ✅ Navigation flow
- ✅ UI/UX polish

Các bài học có thể áp dụng cho các dự án React khác.
