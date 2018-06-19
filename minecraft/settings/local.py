"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to minecraft/settings/local.py. It should not be checked into
your code repository.

"""
from minecraft.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ash', 'ash@dragonpaw.org'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'var/dev.db'),
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'local'


# ROOT_URLCONF = 'minecraft.urls.local'
# WSGI_APPLICATION = 'minecraft.wsgi.local.application'
