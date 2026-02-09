from django.contrib.auth.models import User
from django.db import models

class FavoriteCity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    city = models.CharField(max_length=100)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'city')
        verbose_name_plural = "Favorite Cities"

    def __str__(self):
        return f"{self.city} ({self.user.username})"

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_history')
    city = models.CharField(max_length=100)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Search Histories"
        ordering = ['-searched_at']

    def __str__(self):
        return f"{self.city} - {self.user.username} at {self.searched_at}"
