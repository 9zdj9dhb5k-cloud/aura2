from django.db import models
from django.contrib.auth.models import User

class Perfume(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    notes = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_promo = models.BooleanField(default=False)
    promo_text = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='perfumes/', blank=True, null=True)
    
    in_stock_bishkek_center = models.BooleanField(default=True)
    in_stock_bishkek_asia = models.BooleanField(default=True)
    in_stock_almaty = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} - {self.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'Профиль {self.user.username}'