import random
from decimal import Decimal
from faker import Faker
from langdetect import detect
import os
import re
from django.db import IntegrityError

from .clean_tables import clean_tables
from bookstore.apps.yrb.models import YrbBook, YrbCategory, YrbClub, YrbOffer, YrbShipping

# Clean tables before populating
clean_tables()

# Define language dictionary
language_dict = {
    "af": "Afrikaans", "ar": "Arabic", "bg": "Bulgarian", "bn": "Bengali", "ca": "Catalan", "cs": "Czech",
    "cy": "Welsh", "da": "Danish", "de": "German", "el": "Greek", "en": "English", "es": "Spanish",
    "et": "Estonian", "fa": "Persian", "fi": "Finnish", "fr": "French", "gu": "Gujarati", "he": "Hebrew",
    "hi": "Hindi", "hr": "Croatian", "hu": "Hungarian", "id": "Indonesian", "it": "Italian", "ja": "Japanese",
    "kn": "Kannada", "ko": "Korean", "lt": "Lithuanian", "lv": "Latvian", "mk": "Macedonian", "ml": "Malayalam",
    "mr": "Marathi", "ne": "Nepali", "nl": "Dutch", "no": "Norwegian", "pa": "Punjabi", "pl": "Polish",
    "pt": "Portuguese", "ro": "Romanian", "ru": "Russian", "sk": "Slovak", "sl": "Slovenian", "so": "Somali",
    "sq": "Albanian", "sv": "Swedish", "sw": "Swahili", "ta": "Tamil", "te": "Telugu", "th": "Thai",
    "tl": "Tagalog", "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "vi": "Vietnamese", "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)"
}

fake = Faker()

# Populate YrbCategory
def populate_categories():
    categories = ['children', 'drama', 'horror', 'guide', 'history', 'horror', 'humor', 'mystery', 'philosophy',
                  'religion', 'romance', 'science', 'travel']
    for cat in categories:
        obj, created = YrbCategory.objects.get_or_create(cat=cat)
        if created:
            print(f"Category '{obj.cat}' created successfully.")
        else:
            print(f"Category '{obj.cat}' already exists.")

# Populate YrbClub
def populate_clubs():
    club_names = ['AAA', 'AARP', 'Basic', 'CNU Club', 'Oprah', 'Readers Digest', 'UVA Club', 'VaTech Club', 'W&M Club',
                  'YRB_Bronze', 'YRB_Gold', 'YRB_Silver']
    for name in club_names:
        obj, created = YrbClub.objects.get_or_create(club=name, desp=fake.text(50))
        if created:
            print(f"Club '{obj.club}' created successfully.")
        else:
            print(f"Club '{obj.club}' already exists.")

# Find matching filenames
def find_matching_filenames(folder_path, pattern):
    matching_filenames = []
    for filename in os.listdir(folder_path):
        if re.match(pattern, filename):
            filename_without_extension = os.path.splitext(filename)[0]
            matching_filenames.append(filename_without_extension)
    return matching_filenames

# Format name
def format_name(name):
    return ' '.join(word.capitalize() for word in name.split('-'))

# Populate YrbBook
def populate_books():
    folder_path = './static/images/Books/'
    pattern = r'.*\.jpg$'
    matching_filenames = find_matching_filenames(folder_path, pattern)
    books = []
    for filename in matching_filenames:
        title = format_name(filename)
        year = fake.year()
        language = language_dict[detect(filename)]
        cat = 'religion' if language == 'Urdu' else random.choice(list(YrbCategory.objects.all()))
        weight = random.randint(1, 100)
        books.append(YrbBook(title=title, year=year, language=language, cat=cat, weight=weight))
    YrbBook.objects.bulk_create(books)

# Populate YrbOffer
def populate_offers():
    clubs = list(YrbClub.objects.all())
    for _ in range(1000):
        club = random.choice(clubs)
        title = random.choice(list(YrbBook.objects.all()))
        year = title.year
        price = round(random.uniform(10, 100), 2)
        offerid = fake.unique.random_int(min=1, max=999999)
        try:
            YrbOffer.objects.get_or_create(club=club, title=title, year=year, price=price, offerid=offerid)
        except IntegrityError:
            pass

# Populate YrbShipping
def populate_shipping():
    num_data_points = 5
    step_size = 1000 // (num_data_points - 1)
    shippings = []
    for weight in range(1, 1001, step_size):
        cost = weight * 0.05
        shippings.append(YrbShipping(weight=weight, cost=Decimal(cost)))
    YrbShipping.objects.bulk_create(shippings)

# Main function to populate dummy data
def populate_dummy_data():
    populate_categories()
    populate_clubs()
    populate_books()
    populate_offers()
    populate_shipping()
    print("Dummy data populated successfully!")

populate_dummy_data()
