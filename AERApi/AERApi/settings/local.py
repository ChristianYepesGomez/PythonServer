from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'API_AER',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST':'127.0.0.1',
        # 'PORT':'5432'
        'NAME': 'main',
        'USER': 'main',
        'PASSWORD': 'main',
        'HOST':'127.0.0.1',
        'PORT':'30000'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'