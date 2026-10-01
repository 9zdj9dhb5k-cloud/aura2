import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from appname.models import Perfume

# 1. Очищаем старую базу
Perfume.objects.all().delete()

# 2. Наполняем реальными флаконами
perfumes_data = [
    # --- CLIVE CHRISTIAN (5 шт) ---
    {
        "brand": "Clive Christian",
        "title": "No. 1 Masculine",
        "notes": "Индийский сандал, Кардамон, Мускатный орех, Лайм, Тимьян",
        "price": 72000,
        "is_promo": True,
        "promo_text": "ROYAL 👑",
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Clive Christian",
        "title": "X Feminine",
        "notes": "Египетский жасмин, Персик, Роза, Ваниль, Пачули",
        "price": 54000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": False, "in_stock_almaty": True,
    },
    {
        "brand": "Clive Christian",
        "title": "1872 Masculine",
        "notes": "Птитгрейн, Лайм, Мускатный шалфей, Кедр, Бергамот",
        "price": 43000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Clive Christian",
        "title": "Crab Apple Blossom",
        "notes": "Цвет дикой яблони, Морской аккорд, Мохито, Бергамот, Сандал",
        "price": 48000,
        "is_promo": True,
        "promo_text": "ЭКСКЛЮЗИВ ✨",
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": False, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Clive Christian",
        "title": "Town & Country",
        "notes": "Мускатный шалфей, Амбра, Сосновые иголки, Кардамон, Белый кедр",
        "price": 49000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": False,
    },

    # --- LOUIS VUITTON (5 шт) ---
    {
        "brand": "Louis Vuitton",
        "title": "Ombre Nomade",
        "notes": "Уд, Ладан, Малина, Береза, Шафран, Роза",
        "price": 42000,
        "is_promo": True,
        "promo_text": "БЕСТСЕЛЛЕР 🔥",
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Louis Vuitton",
        "title": "Imagination",
        "notes": "Амброксан, Китайский черный чай, Калабрийский цитрус, Имбирь, Нероли",
        "price": 35000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Louis Vuitton",
        "title": "L'Immensité",
        "notes": "Грейпфрут, Имбирь, Бергамот, Шалфей, Розмарин, Амброксан",
        "price": 35000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": False, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Louis Vuitton",
        "title": "Attrape-Rêves",
        "notes": "Какао, Пион, Личи, Пачули, Имбирь, Турецкая роза",
        "price": 35000,
        "is_promo": True,
        "promo_text": "ТОП ВЫБОР ❤️",
        "image": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": False, "in_stock_almaty": True,
    },
    {
        "brand": "Louis Vuitton",
        "title": "Pacific Chill",
        "notes": "Черная смородина, Мята, Лимон, Базилик, Семена моркови, Майская роза",
        "price": 35000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },

    # --- ТОПОВЫЕ НИШЕВЫЕ ХИТЫ ---
    {
        "brand": "Maison Francis Kurkdjian",
        "title": "Baccarat Rouge 540",
        "notes": "Шафран, Жасмин, Древесный янтарь, Серая амбра, Еловая смола",
        "price": 38500,
        "is_promo": True,
        "promo_text": "ХИТ ПРОДАЖ 🔥",
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Creed",
        "title": "Aventus",
        "notes": "Ананас, Бергамот, Чёрная смородина, Береза, Пачули, Мускус",
        "price": 42000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": False, "in_stock_almaty": True,
    },
    {
        "brand": "Tom Ford",
        "title": "Lost Cherry",
        "notes": "Вишня, Горький миндаль, Ликер, Слива, Турецкая роза, Перуанский бальзам",
        "price": 45000,
        "is_promo": True,
        "promo_text": "СКИДКА 10%",
        "image": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": False,
    },
    {
        "brand": "Ex Nihilo",
        "title": "Fleur Narcotique",
        "notes": "Пион, Бергамот, Личи, Персик, Цветки апельсина, Мускус",
        "price": 31000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Parfums de Marly",
        "title": "Delina",
        "notes": "Ревень, Личи, Бергамот, Турецкая роза, Пион, Ваниль, Кашмеран",
        "price": 33000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": False, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Byredo",
        "title": "Bal d'Afrique",
        "notes": "Бархатцы, Лимон, Бергамот, Фиалка, Цикламен, Ветивер, Серая амбра",
        "price": 31000,
        "is_promo": True,
        "promo_text": "ТОП ВЫБОР ✨",
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },

    # --- ЭКСПЕРТНАЯ НИША И АВАНГАРД ---
    {
        "brand": "Marc-Antoine Barrois",
        "title": "Ganymede",
        "notes": "Замша, Бессмертник, Итальянский мандарин, Османтус, Акигалавуд",
        "price": 23000,
        "is_promo": True,
        "promo_text": "ТРЕНД ⚡",
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Stéphane Humbert Lucas 777",
        "title": "God of Fire",
        "notes": "Манго, Лимон, Розовый перец, Имбирь, Кумарин, Уд, Нагармота",
        "price": 32000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": False, "in_stock_almaty": True,
    },
    {
        "brand": "BDK Parfums",
        "title": "Gris Charnel Extrait",
        "notes": "Черный чай, Кардамон, Инжир, Ирис, Бурбонская ваниль, Сандал",
        "price": 28000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Orto Parisi",
        "title": "Megamare",
        "notes": "Морские водоросли, Морская соль, Амбра, Древесные ноты, Мускус",
        "price": 21000,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": False, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    },
    {
        "brand": "Kilian",
        "title": "Angels' Share",
        "notes": "Коньяк, Корица, Бобы тонка, Дуб, Пралине, Ваниль, Сандал",
        "price": 34000,
        "is_promo": True,
        "promo_text": "БЕСТСЕЛЛЕР 🥃",
        "image": "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": False,
    },
    {
        "brand": "Xerjoff",
        "title": "Erba Pura",
        "notes": "Сицилийский апельсин, Бергамот, Фруктовые ноты, Белый мускус, Ваниль",
        "price": 27500,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": False, "in_stock_almaty": True,
    },
    {
        "brand": "Maison Margiela",
        "title": "Replica Jazz Club",
        "notes": "Ром, Розовый перец, Нероли, Табачный лист, Ваниль, Стиракс",
        "price": 18500,
        "is_promo": False,
        "image": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&auto=format&fit=crop",
        "in_stock_bishkek_center": True, "in_stock_bishkek_asia": True, "in_stock_almaty": True,
    }
]

for item in perfumes_data:
    Perfume.objects.create(**item)

print(f"🎉 Успешно обновлено {len(perfumes_data)} парфюмов!")