# 🌦️ NepWeather: Premium Meteorological Dashboard

[![Django](https://img.shields.io/badge/Django-5.0+-092e20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![UI](https://img.shields.io/badge/UI-Glassmorphism-38bdf8?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)

**NepWeather** is a sophisticated, real-time weather analytics platform built with Django. It bridges the gap between powerful backend logic and a stunning, high-performance glassmorphic user interface. Designed for professionals and enthusiasts alike, it provides precise meteorological insights with a premium aesthetic.

---

## 🚀 Key Features

- **🌐 Global Reach**: Instant real-time weather data for millions of locations worldwide via [WeatherAPI](https://www.weatherapi.com/).
- **📈 Advanced Analytics**: Interactive **Chart.js** integration providing visualized 5-day temperature trends.
- **🛡️ Secure Pro Auth**: Enterprise-grade authentication system allowing users to save personal preferences and locations.
- **✨ Dynamic Environment**: A "Living UI" that automatically adapts its theme, gradients, and animations based on live weather conditions (Sunny, Cloudy, Rainy, Snowy, or Stormy).
- **⭐ Saved Locations**: One-click "Star" functionality to manage your most-watched cities.
- **🕒 Intelligent History**: Smart search tracking that automatically prioritizes recently viewed locations with improved timestamp logic.
- **⚡ Performance First**: Implements Django's file-based caching and session management for sub-second response times.
- **📱 Ultra-Responsive**: Pixel-perfect layouts optimized for everything from mobile devices to ultra-wide monitors.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.10+, Django 5.x |
| **Frontend** | HTML5, CSS3 (Glassmorphism), JavaScript (ES6+) |
| **Data Viz** | Chart.js 4.x |
| **Styling** | Vanilla CSS (Custom Design System), Bootstrap 5.3 (Grid) |
| **Icons** | FontAwesome 6 (Lucide-inspired) |
| **Database** | SQLite3 (Persistent storage for favorites/history) |
| **API** | WeatherAPI.com (Weather & Forecast JSON API) |

---

## 🏁 Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher.
- A WeatherAPI key (Get one for free at [WeatherAPI.com](https://www.weatherapi.com/)).

### 2. Implementation
Clone the repository and enter the project directory:
```bash
git clone https://github.com/yourusername/NepWeather.git
cd NepWeather/weather_project
```

Install the production-ready dependencies:
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secure-django-key
WEATHER_API_KEY=your-api-key-from-weatherapi
DEBUG=True
```

### 4. Initialize Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Launch
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` to experience **NepWeather**.

---

## 📂 Project Architecture

```text
weather_project/
├── weather/               
│   ├── templatetags/     # Custom meteorological filters (e.g., split)
│   ├── models.py         # Favorite and Search History schemas
│   ├── views.py          # Weather processing & API logic
│   └── forms.py          # Clean, modern user registration
├── templates/            
│   ├── base.html         # Premium glass design system
│   └── weather/          # Context-aware dashboards
├── .env                  # Environment-specific configuration
└── manage.py             # System entry point
```

---

## 🎨 UI Design Philosophy
The platform is built on **Modern Glassmorphism** principles:
- **Translucency**: Multi-layered backdrop blurs create depth and focus.
- **Vibrant Accents**: Use of `38bdf8` (Sky Blue) to highlight critical data points.
- **Micro-Animations**: Floating weather icons and smooth entry transitions for enhanced engagement.
- **Dynamic Theming**: CSS variables that update via JavaScript based on Weather Condition Codes.

---

---

## � Deployment Guide

This project is configured for easy deployment on **Railway**, **Heroku**, or **Render**.

### 1. Production Hardening
The application has been pre-configured with:
- **WhiteNoise**: Efficient static file serving & compression.
- **Gunicorn**: Industrial-strength WSGI HTTP Server.
- **Security Middleware**: Automatic SSL redirects and header protection when `DEBUG=False`.

### 2. Environment Variables
Ensure the following variables are set in your deployment platform's dashboard:
- `DEBUG`: Set to `False`.
- `ALLOWED_HOSTS`: Your domain (e.g., `yourapp.up.railway.app`).
- `WEATHER_API_KEY`: Your WeatherAPI key.
- `SECRET_KEY`: A random, secure string.
- `SECURE_SSL_REDIRECT`: Set to `True` for HTTPS.

---

## ⚡ Performance Optimization
- **Caching**: The app uses `FileBasedCache` to minimize API calls and speed up response times for frequently searched cities.
- **Static Assets**: CSS and JS files are compressed and cached using WhiteNoise's `ManifestStaticFilesStorage`.

---

## 📄 License
Licensed under the **MIT License**.
