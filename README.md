# Weather Dashboard 🌤️

یک داشبورد هواشناسی مدرن که اطلاعات آب‌وهوای real-time را از API عمومی OpenWeatherMap دریافت می‌کند.

## ✨ ویژگی‌ها:

- 🌍 **جستجوی شهر** - جستجوی هواشناسی هر شهر
- 🌡️ **دما و احساس** - نمایش دمای واقعی و احساس‌شده
- 💧 **رطوبت و فشار** - اطلاعات دقیق رطوبت و فشار جو
- 💨 **سرعت و جهت باد** - اطلاعات جزئی باد
- ⏰ **زمان به‌روزرسانی** - آخرین زمان دریافت اطلاعات
- 🎨 **رابط کاربری جذاب** - طراحی مدرن و حرفه‌ای
- ⚡ **کارایی بالا** - thread‌های جداگانه برای دریافت داده

## 📋 نیازمندی‌ها:

- Python 3.7+
- requests
- Pillow (PIL)
- tkinter (معمولاً با Python نصب می‌شود)

## 🚀 نحوه استفاده:

### روش 1: اجرای فایل Python
```bash
pip install -r requirements.txt
python weather_dashboard.py
```

### روش 2: اجرای فایل .exe (بدون Python)
1. فایل `build.bat` را دوبل کلیک کنید
2. صبر کنید تا `Weather Dashboard.exe` ساخته شود
3. فایل .exe را اجرا کنید

## ⚙️ تنظیمات:

تمام تنظیمات در فایل `config.py` موجود است:

```python
API_KEY = "your-api-key"  # API Key از OpenWeatherMap
UNITS = "metric"           # metric (Celsius) یا imperial (Fahrenheit)
DEFAULT_CITY = "London"    # شهر پیش‌فرض
```

## 🔑 دریافت API Key:

1. سایت OpenWeatherMap را بازکنید: https://openweathermap.org/api
2. ثبت‌نام کنید (رایگان)
3. API Key خود را کپی کنید
4. API Key را در `config.py` قرار دهید

## 📸 نمایش:

```
🌤️ Weather Dashboard
┌─────────────────────────────┐
│ Enter City:  [London    ] 🔍 │
├─────────────────────────────┤
│ 🌍 Location: London, UK      │
│ 🌡️ Temp: 15°C (Feels: 14°C) │
│ 📝 Condition: Cloudy         │
│ 💧 Humidity: 72%             │
│ 🔽 Pressure: 1013 hPa        │
│ 💨 Wind: 8 m/s               │
└─────────────────────────────┘
```

## 🔄 به‌روزرسانی خودکار:

داشبورد هر 5 دقیقه به‌طور خودکار اطلاعات را به‌روزرسانی می‌کند (قابل تغییر در `config.py`).

## 📝 لایسنس:

MIT License - آزادانه استفاده کنید!

## 🤝 مشارکت:

برای مشارکت، Pull Request ارسال کنید!

---

**ساخته شده با ❤️ برای عاشقان هواشناسی**
