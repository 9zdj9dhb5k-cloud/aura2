from django.contrib import admin
from .models import Perfume, Profile

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'title', 'price', 'is_promo', 'in_stock_bishkek_center', 'in_stock_bishkek_asia', 'in_stock_almaty')
    list_filter = ('brand', 'is_promo', 'in_stock_bishkek_center', 'in_stock_bishkek_asia', 'in_stock_almaty')
    search_fields = ('brand', 'title', 'notes')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')