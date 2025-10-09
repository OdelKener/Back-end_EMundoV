from .base import *
from decouple import config
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['ediciones-mundo-backend.onrender.com', 'localhost', '127.0.0.1']

# Database - Usar PostgreSQL en producción
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')