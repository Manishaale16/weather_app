from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('toggle-unit/', views.toggle_unit, name='toggle_unit'),
    path('add-favorite/<str:city>/', views.add_favorite, name='add_favorite'),
    path('remove-favorite/<str:city>/', views.remove_favorite, name='remove_favorite'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
