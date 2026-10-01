from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Perfume, Profile

def index(request):
    current_store = request.GET.get('store', 'bishkek_center')
    
    if current_store == 'bishkek_asia':
        perfumes = Perfume.objects.filter(in_stock_bishkek_asia=True)
    elif current_store == 'almaty':
        perfumes = Perfume.objects.filter(in_stock_almaty=True)
    else:
        perfumes = Perfume.objects.filter(in_stock_bishkek_center=True)
        
    user_favorites = request.session.get('favorites', [])
    
    profile = None
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
    
    context = {
        'perfumes': perfumes,
        'current_store': current_store,
        'user_favorites': user_favorites,
        'profile': profile,
    }
    return render(request, 'appname/index.html', context)

def favorites(request):
    fav_ids = request.session.get('favorites', [])
    perfumes = Perfume.objects.filter(id__in=fav_ids)
    
    profile = None
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
    
    context = {
        'perfumes': perfumes,
        'user_favorites': fav_ids,
        'profile': profile,
    }
    return render(request, 'appname/favorites.html', context)

def toggle_favorite(request, perfume_id):
    favorites_list = request.session.get('favorites', [])
    
    if perfume_id in favorites_list:
        favorites_list.remove(perfume_id)
    else:
        favorites_list.append(perfume_id)
        
    request.session['favorites'] = favorites_list
    request.session.modified = True
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart(request):
    cart_dict = request.session.get('cart', {})
    perfume_ids = list(cart_dict.keys())
    perfumes = Perfume.objects.filter(id__in=perfume_ids)
    
    cart_items = []
    total_price = 0
    for perfume in perfumes:
        quantity = cart_dict.get(str(perfume.id), 1)
        item_total = perfume.price * quantity
        total_price += item_total
        cart_items.append({
            'perfume': perfume,
            'quantity': quantity,
            'item_total': item_total,
        })
        
    profile = None
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'profile': profile,
    }
    return render(request, 'appname/cart.html', context)

def add_to_cart(request, perfume_id):
    cart_dict = request.session.get('cart', {})
    str_id = str(perfume_id)
    cart_dict[str_id] = cart_dict.get(str_id, 0) + 1
    request.session['cart'] = cart_dict
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST' and request.FILES.get('avatar'):
        profile.avatar = request.FILES['avatar']
        profile.save()
        return redirect('profile')
        
    return render(request, 'appname/profile.html', {'profile': profile})