import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import {
  ArrowRight,
  ChevronLeft,
  ChevronRight,
  ShieldCheck,
  Sparkles,
  Truck,
} from 'lucide-react';

const heroSlides = [
  {
    id: 1,
    badge: 'Bộ sưu tập mới',
    title: 'Mua sắm thông minh, nâng tầm phong cách sống',
    description:
      'Khám phá hàng ngàn sản phẩm hiện đại với thiết kế đẹp, giá tốt và giao hàng nhanh trên toàn quốc.',
    image:
      'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80',
    primaryCta: 'Shop Now',
    secondaryCta: 'View Products',
  },
  {
    id: 2,
    badge: 'Ưu đãi cuối tuần',
    title: 'Giảm giá đến 50% cho các sản phẩm nổi bật',
    description:
      'Săn deal hot cho công nghệ, thời trang và phụ kiện với nhiều ưu đãi độc quyền chỉ có hôm nay.',
    image:
      'https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=900&q=80',
    primaryCta: 'Mua ngay',
    secondaryCta: 'Xem khuyến mãi',
  },
  {
    id: 3,
    badge: 'Hàng tuyển chọn',
    title: 'Sản phẩm chất lượng cho mọi nhu cầu mỗi ngày',
    description:
      'Từ đồ công nghệ đến lifestyle essentials, mọi thứ bạn cần đều có trong một trải nghiệm mua sắm tiện lợi.',
    image:
      'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?auto=format&fit=crop&w=900&q=80',
    primaryCta: 'Khám phá ngay',
    secondaryCta: 'Xem tất cả',
  },
];

const featuredProducts = [
  {
    id: 1,
    name: 'Tai nghe Bluetooth ProSound X5',
    price: '1.299.000đ',
    oldPrice: '1.690.000đ',
    image:
      'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80',
    tag: 'Best Seller',
  },
  {
    id: 2,
    name: 'Áo khoác Urban Streetwear',
    price: '699.000đ',
    oldPrice: '899.000đ',
    image:
      'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=800&q=80',
    tag: 'New Arrival',
  },
  {
    id: 3,
    name: 'Đồng hồ thông minh Active Fit',
    price: '2.190.000đ',
    oldPrice: '2.590.000đ',
    image:
      'https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&fit=crop&w=800&q=80',
    tag: 'Hot Deal',
  },
  {
    id: 4,
    name: 'Balo Laptop Minimal 15.6 inch',
    price: '459.000đ',
    oldPrice: '590.000đ',
    image:
      'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80',
    tag: 'Trending',
  },
];

const categories = [
  {
    name: 'Điện tử',
    icon: '📱',
    description: 'Thiết bị công nghệ, phụ kiện hiện đại',
    color: 'from-blue-500 to-cyan-500',
  },
  {
    name: 'Thời trang',
    icon: '👗',
    description: 'Phong cách trẻ trung, đa dạng xu hướng',
    color: 'from-pink-500 to-rose-500',
  },
  {
    name: 'Phụ kiện',
    icon: '⌚',
    description: 'Nhỏ gọn, tinh tế và tiện dụng hằng ngày',
    color: 'from-amber-500 to-orange-500',
  },
  {
    name: 'Lifestyle',
    icon: '🏠',
    description: 'Sản phẩm nâng cấp không gian sống',
    color: 'from-emerald-500 to-teal-500',
  },
];

const highlights = [
  {
    icon: Truck,
    title: 'Giao hàng nhanh',
    description: 'Nhận hàng toàn quốc chỉ từ 2-4 ngày.',
  },
  {
    icon: ShieldCheck,
    title: 'Bảo đảm chất lượng',
    description: 'Sản phẩm được tuyển chọn từ nhà bán uy tín.',
  },
  {
    icon: Sparkles,
    title: 'Ưu đãi mỗi tuần',
    description: 'Liên tục cập nhật deal hot và voucher mới.',
  },
];

export default function Home() {
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % heroSlides.length);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const nextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % heroSlides.length);
  };

  const prevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + heroSlides.length) % heroSlides.length);
  };

  const activeSlide = heroSlides[currentSlide];

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <section className="relative overflow-hidden bg-slate-950">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-700/30 via-cyan-500/10 to-transparent" />
        <div className="absolute -top-24 right-0 h-72 w-72 rounded-full bg-cyan-400/20 blur-3xl" />
        <div className="absolute bottom-0 left-0 h-72 w-72 rounded-full bg-blue-600/20 blur-3xl" />

        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
          <div className="grid items-center gap-10 lg:grid-cols-2">
            <div className="text-white">
              <span className="inline-flex items-center rounded-full border border-white/20 bg-white/10 px-4 py-1 text-sm font-medium backdrop-blur">
                {activeSlide.badge}
              </span>
              <h1 className="mt-6 text-4xl font-bold leading-tight sm:text-5xl lg:text-6xl">
                {activeSlide.title}
              </h1>
              <p className="mt-5 max-w-xl text-base text-slate-200 sm:text-lg">
                {activeSlide.description}
              </p>

              <div className="mt-8 flex flex-col gap-4 sm:flex-row">
                <Link
                  to="/products"
                  className="inline-flex items-center justify-center gap-2 rounded-full bg-white px-6 py-3 font-semibold text-slate-900 transition hover:bg-slate-100"
                >
                  {activeSlide.primaryCta}
                  <ArrowRight size={18} />
                </Link>
                <Link
                  to="/products"
                  className="inline-flex items-center justify-center rounded-full border border-white/30 px-6 py-3 font-semibold text-white transition hover:bg-white/10"
                >
                  {activeSlide.secondaryCta}
                </Link>
              </div>

              <div className="mt-10 grid gap-4 sm:grid-cols-3">
                {highlights.map((item) => {
                  const Icon = item.icon;
                  return (
                    <div
                      key={item.title}
                      className="rounded-2xl border border-white/10 bg-white/5 p-4 backdrop-blur-sm"
                    >
                      <Icon className="mb-3 text-cyan-300" size={22} />
                      <h3 className="font-semibold">{item.title}</h3>
                      <p className="mt-1 text-sm text-slate-300">{item.description}</p>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="relative">
              <div className="absolute -inset-4 rounded-[2rem] bg-gradient-to-tr from-cyan-400/30 to-blue-600/20 blur-2xl" />
              <div className="relative overflow-hidden rounded-[2rem] border border-white/10 bg-white/10 shadow-2xl backdrop-blur-sm">
                <img
                  src={activeSlide.image}
                  alt={activeSlide.title}
                  className="h-[320px] w-full object-cover sm:h-[420px] lg:h-[500px]"
                />
                <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-slate-950/80 to-transparent p-6 text-white">
                  <p className="text-sm uppercase tracking-[0.3em] text-cyan-300">ShopHub</p>
                  <h2 className="mt-2 text-2xl font-semibold">Ưu đãi nổi bật mỗi ngày</h2>
                  <p className="mt-2 text-sm text-slate-200 sm:text-base">
                    Cập nhật xu hướng mua sắm mới nhất với thiết kế hiện đại và trải nghiệm tối ưu trên mọi thiết bị.
                  </p>
                </div>
              </div>

              <div className="mt-6 flex items-center justify-between">
                <div className="flex items-center gap-2">
                  {heroSlides.map((slide, index) => (
                    <button
                      key={slide.id}
                      type="button"
                      onClick={() => setCurrentSlide(index)}
                      className={`h-2.5 rounded-full transition-all ${
                        currentSlide === index ? 'w-8 bg-white' : 'w-2.5 bg-white/40'
                      }`}
                      aria-label={`Chuyển đến slide ${index + 1}`}
                    />
                  ))}
                </div>

                <div className="flex gap-3">
                  <button
                    type="button"
                    onClick={prevSlide}
                    className="inline-flex h-11 w-11 items-center justify-center rounded-full border border-white/20 bg-white/10 text-white transition hover:bg-white/20"
                    aria-label="Slide trước"
                  >
                    <ChevronLeft size={20} />
                  </button>
                  <button
                    type="button"
                    onClick={nextSlide}
                    className="inline-flex h-11 w-11 items-center justify-center rounded-full border border-white/20 bg-white/10 text-white transition hover:bg-white/20"
                    aria-label="Slide tiếp theo"
                  >
                    <ChevronRight size={20} />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="py-16 sm:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-10 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-600">
                Featured Products
              </p>
              <h2 className="mt-3 text-3xl font-bold sm:text-4xl">Sản phẩm nổi bật</h2>
              <p className="mt-3 max-w-2xl text-slate-600">
                Những lựa chọn được yêu thích nhất tuần này với thiết kế đẹp, giá tốt và phù hợp nhiều nhu cầu sử dụng.
              </p>
            </div>
            <Link
              to="/products"
              className="inline-flex items-center gap-2 self-start rounded-full border border-slate-300 px-5 py-3 font-semibold text-slate-800 transition hover:border-blue-600 hover:text-blue-600"
            >
              View Products
              <ArrowRight size={18} />
            </Link>
          </div>

          <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">
            {featuredProducts.map((product) => (
              <div
                key={product.id}
                className="group overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-sm transition duration-300 hover:-translate-y-1 hover:shadow-xl"
              >
                <div className="relative overflow-hidden">
                  <img
                    src={product.image}
                    alt={product.name}
                    className="h-64 w-full object-cover transition duration-500 group-hover:scale-105"
                  />
                  <span className="absolute left-4 top-4 rounded-full bg-slate-950 px-3 py-1 text-xs font-semibold text-white">
                    {product.tag}
                  </span>
                </div>
                <div className="p-5">
                  <h3 className="text-lg font-semibold text-slate-900">{product.name}</h3>
                  <div className="mt-3 flex items-center gap-3">
                    <span className="text-xl font-bold text-blue-600">{product.price}</span>
                    <span className="text-sm text-slate-400 line-through">{product.oldPrice}</span>
                  </div>
                  <div className="mt-5 flex gap-3">
                    <button className="flex-1 rounded-full bg-slate-950 px-4 py-3 font-medium text-white transition hover:bg-blue-600">
                      Thêm vào giỏ
                    </button>
                    <Link
                      to="/products"
                      className="inline-flex items-center justify-center rounded-full border border-slate-300 px-4 py-3 text-slate-700 transition hover:border-blue-600 hover:text-blue-600"
                    >
                      Xem
                    </Link>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-white py-16 sm:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-10 text-center">
            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-600">
              Categories
            </p>
            <h2 className="mt-3 text-3xl font-bold sm:text-4xl">Mua sắm theo danh mục</h2>
            <p className="mt-4 text-slate-600">
              Chọn nhanh danh mục yêu thích để khám phá sản phẩm phù hợp với phong cách và nhu cầu của anh.
            </p>
          </div>

          <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">
            {categories.map((category) => (
              <Link
                key={category.name}
                to={`/products?category=${encodeURIComponent(category.name.toLowerCase())}`}
                className="group relative overflow-hidden rounded-3xl border border-slate-200 bg-slate-50 p-6 transition duration-300 hover:-translate-y-1 hover:shadow-xl"
              >
                <div
                  className={`absolute inset-x-0 top-0 h-1.5 bg-gradient-to-r ${category.color}`}
                />
                <div className="mb-5 inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-white text-3xl shadow-sm transition group-hover:scale-110">
                  {category.icon}
                </div>
                <h3 className="text-xl font-semibold text-slate-900">{category.name}</h3>
                <p className="mt-3 text-sm leading-6 text-slate-600">{category.description}</p>
                <div className="mt-6 inline-flex items-center gap-2 font-medium text-blue-600">
                  Khám phá ngay
                  <ArrowRight size={18} />
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      <section className="pb-16 sm:pb-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="overflow-hidden rounded-[2rem] bg-gradient-to-r from-blue-600 via-cyan-500 to-teal-500 px-6 py-10 text-white shadow-xl sm:px-10 lg:px-14 lg:py-14">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
              <div className="max-w-2xl">
                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-white/80">
                  Limited Offer
                </p>
                <h2 className="mt-3 text-3xl font-bold sm:text-4xl">
                  Sẵn sàng khám phá bộ sưu tập mới hôm nay?
                </h2>
                <p className="mt-4 text-white/90">
                  Mở ra trải nghiệm mua sắm trực quan, nhanh chóng và đầy cảm hứng với các sản phẩm đang được yêu thích nhất.
                </p>
              </div>

              <div className="flex flex-col gap-4 sm:flex-row">
                <Link
                  to="/products"
                  className="inline-flex items-center justify-center rounded-full bg-white px-6 py-3 font-semibold text-slate-900 transition hover:bg-slate-100"
                >
                  Shop Now
                </Link>
                <Link
                  to="/products"
                  className="inline-flex items-center justify-center rounded-full border border-white/40 px-6 py-3 font-semibold text-white transition hover:bg-white/10"
                >
                  View Products
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
