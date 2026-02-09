from django.contrib import admin
from .models import FavoriteCity, SearchHistory

@admin.register(FavoriteCity)
class FavoriteCityAdmin(admin.ModelAdmin):
    list_display = ('city', 'user', 'added_at')
    search_fields = ('city', 'user__username')
    list_filter = ('added_at',)

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city', 'user', 'searched_at')
    search_fields = ('city', 'user__username')
    list_filter = ('searched_at',)
