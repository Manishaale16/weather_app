import os
import requests

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

from .models import FavoriteCity, SearchHistory
from .forms import CustomUserCreationForm


API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/"


def get_weather_data(city, units='metric'):
    cache_key = f"weather_data_v2_{city}_{units}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data, None

    try:
        url = f"{BASE_URL}forecast.json?key={API_KEY}&q={city}&days=5&alerts=yes"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return None, data.get("error", {}).get("message", "City not found")

        curr = data['current']
        loc = data['location']
        unit_label = '°C' if units == 'metric' else '°F'

        temp = curr['temp_c'] if units == 'metric' else curr['temp_f']
        feels = curr['feelslike_c'] if units == 'metric' else curr['feelslike_f']
        vis = curr['vis_km'] if units == 'metric' else curr['vis_miles']
        precip = curr['precip_mm'] if units == 'metric' else curr['precip_in']

        wind = curr['wind_kph']
        if units == 'metric':
            wind = round(wind / 3.6, 1)

        processed_current = {
            'temp': f"{temp:.0f}{unit_label}",
            'feels_like': f"{feels:.0f}{unit_label}",
            'humidity': f"{curr['humidity']}%",
            'wind_speed': f"{wind} {'m/s' if units == 'metric' else 'mph'}",
            'pressure': f"{curr['pressure_mb']} hPa",
            'uv': curr['uv'],
            'visibility': f"{vis} {'km' if units == 'metric' else 'mi'}",
            'precip': f"{precip} {'mm' if units == 'metric' else 'in'}",
            'condition': curr['condition']['text'],
            'condition_code': curr['condition']['code'],
            'icon': "https:" + curr['condition']['icon'],
        }

        processed_forecast = []
        raw_temps = []
        for day in data['forecast']['forecastday']:
            avg = day['day']['avgtemp_c'] if units == 'metric' else day['day']['avgtemp_f']
            processed_forecast.append({
                'date': day['date'],
                'temp': f"{avg:.0f}{unit_label}",
                'condition': day['day']['condition']['text'],
                'icon': "https:" + day['day']['condition']['icon'],
                'rain_chance': f"{day['day']['daily_chance_of_rain']}%",
            })
            raw_temps.append(round(avg, 1))

        processed_alerts = []
        if 'alerts' in data and 'alert' in data['alerts']:
            for alert in data['alerts']['alert']:
                processed_alerts.append({
                    'headline': alert.get('headline'),
                    'severity': alert.get('severity'),
                    'description': alert.get('desc'),
                })

        result = {
            'city': loc['name'],
            'country': loc['country'],
            'current': processed_current,
            'forecast': processed_forecast,
            'raw_temps': raw_temps,
            'alerts': processed_alerts,
        }

        cache.set(cache_key, result, 600)
        return result, None

    except Exception:
        return None, "Unable to fetch weather data."


def home(request):
    city_query = request.GET.get('city')
    unit_pref = request.session.get('units', 'metric')

    weather, error = None, None
    if city_query:
        weather, error = get_weather_data(city_query, unit_pref)

    favs = []
    history = []
    is_fav = False

    if request.user.is_authenticated:
        if weather and not error:
            # Update history: if exists, update timestamp; else create.
            history_item, created = SearchHistory.objects.get_or_create(
                user=request.user, city=weather['city']
            )
            if not created:
                from django.utils import timezone
                history_item.searched_at = timezone.now()
                history_item.save()

        favs = FavoriteCity.objects.filter(user=request.user)
        history = SearchHistory.objects.filter(user=request.user)[:5]

        if weather:
            is_fav = FavoriteCity.objects.filter(
                user=request.user, city=weather['city']
            ).exists()

    context = {
        'weather': weather,
        'error': error,
        'units': unit_pref,
        'city': city_query,
        'favorites': favs,
        'history': history,
        'is_favorite': is_fav,
    }
    return render(request, 'weather/index.html', context)


def toggle_unit(request):
    request.session['units'] = (
        'imperial'
        if request.session.get('units', 'metric') == 'metric'
        else 'metric'
    )
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_favorite(request, city):
    FavoriteCity.objects.get_or_create(user=request.user, city=city)
    return redirect('home')


@login_required
def remove_favorite(request, city):
    FavoriteCity.objects.filter(user=request.user, city=city).delete()
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'weather/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'weather/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
