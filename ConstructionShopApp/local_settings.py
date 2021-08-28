# SECURITY WARNING: keep the secret key used in production secret!
from ConstructionShopApp.settings import BASE_DIR

SECRET_KEY = 'django-insecure-d^nai9h)s$5n%f@@g-3q*4eio7uc%4grcf*omtw9(hfqwztz=*'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store',
        'HOST': 'localhost',
        'PASSWORD': 'admin',
        'USER': 'postgres',
        'PORT': 5432
    }
}