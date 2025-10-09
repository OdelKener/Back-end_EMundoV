from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['*']

# Ya debería usar SQLite de base.py
# No necesitamos redefinir DATABASES aquí

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')