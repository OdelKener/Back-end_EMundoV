from .base import *

DEBUG = True

# ALLOWED_HOSTS
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost',
    '.ngrok-free.app',
    '979421631b87.ngrok-free.app'
]

# CSRF TRUSTED ORIGINS (AGREGA ESTO)
CSRF_TRUSTED_ORIGINS = [
    'https://979421631b87.ngrok-free.app',
    'https://*.ngrok-free.app',
]

# CORS CONFIGURATION (AGREGA ESTO TAMBIÉN)
CORS_ALLOWED_ORIGINS = [
    "https://979421631b87.ngrok-free.app",
    "https://interfazweb-emundo-v.netlify.app",
]

CORS_ALLOW_CREDENTIALS = True

# Tu configuración de base de datos igual...
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'EdicionesMundoInvIntegral',
        'HOST': 'KABRONKTOM\\MSSQLSERVER300',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
            'extra_params': 'TrustServerCertificate=yes',
        },
    }
}
