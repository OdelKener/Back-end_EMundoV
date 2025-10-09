from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['ediciones-mundo-backend.onrender.com', 'localhost', '127.0.0.1', '.onrender.com', '*']

# Database - SQLite simple
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Security settings
SECURE_SSL_REDIRECT = False  # Desactivar temporalmente
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')