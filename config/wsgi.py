import os

from django.core.wsgi import get_wsgi_application

# ✅ CAMBIAR de 'config.base' a 'config.dev'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.dev')

application = get_wsgi_application()
