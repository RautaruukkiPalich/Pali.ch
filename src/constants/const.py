import os
from string import ascii_letters, digits

SYMBOLS = ascii_letters + digits
"""
HOST_URL = "https://pali.ch/
"""
HOST_URL = os.environ.get(f"HOST_URL", "localhost:8000/")

POPULAR_URLS = [
    "vk.com",
    "google.com",
    "wikipedia",
    "yandex",
    "ya.ru",
]
