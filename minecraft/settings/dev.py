"""Settings for Development Server"""
from minecraft.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

VAR_ROOT = '/var/www/dpminecraft'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dpminecraft',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dev'

# WSGI_APPLICATION = 'minecraft.wsgi.dev.application'
