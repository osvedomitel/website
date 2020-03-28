import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


"""
Security
"""

SECRET_KEY = 'generate_a_long_random_string_and_place_it_here'
DEBUG = True
ALLOWED_HOSTS = []

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False


"""
Static and media
"""

STATIC_ROOT = os.path.join(BASE_DIR, 'static/dist')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


"""
Databases
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}


"""
Email
"""

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL = 'django@localhost'

ADMINS = [('me', 'human@localhost'),]
