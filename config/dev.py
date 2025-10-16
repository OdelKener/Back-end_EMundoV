DEBUG = True

# ALLOWED_HOSTS - MÁS FLEXIBLE PARA NGROK
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost',
    '.ngrok-free.app',
    'afdd34068c0c.ngrok-free.app',
    'localhost:8000',  # ← AGREGAR ESTO
]

# CSRF TRUSTED ORIGINS (ACTUALIZADO)
CSRF_TRUSTED_ORIGINS = [
    'https://afdd34068c0c.ngrok-free.app',
    'https://*.ngrok-free.app',
    'http://localhost:8000',  # ← AGREGAR ESTO
    'http://127.0.0.1:8000',  # ← AGREGAR ESTO
]

# CORS CONFIGURATION (ACTUALIZADO)
CORS_ALLOWED_ORIGINS = [
    "https://afdd34068c0c.ngrok-free.app",
    "https://interfazweb-emundo-v.netlify.app",
    "http://localhost:8000",  # ← AGREGAR ESTO
    "http://127.0.0.1:8000",  # ← AGREGAR ESTO
]

CORS_ALLOW_CREDENTIALS = True

# CORS ADDITIONAL SETTINGS (NUEVO)
CORS_ALLOW_ALL_ORIGINS = True  # Solo para desarrollo
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# SESSION AND CSRF COOKIE (NUEVO)
CSRF_COOKIE_SECURE = False  # False para desarrollo
SESSION_COOKIE_SECURE = False  # False para desarrollo
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# Tu configuración de base de datos...
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