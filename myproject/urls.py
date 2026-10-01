from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appname import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('favorites/', views.favorites, name='favorites'),
    path('toggle-favorite/<int:perfume_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:perfume_id>/', views.add_to_cart, name='add_to_cart'),
    path('profile/', views.profile_view, name='profile'),
]

# Раздача загруженных картинок (аватарок и медиа) в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)