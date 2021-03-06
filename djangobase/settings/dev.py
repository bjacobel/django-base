from djangobase.settings.common import *
import yaml

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = 'afakesecretkeyfordevelopment'

SECURE_SSL_REDIRECT = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': SITE_NAME,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ALLOWED_HOSTS = [
    '*'
]

INTERNAL_IPS = (
    '127.0.0.1',
    '0.0.0.0'
)

INSTALLED_APPS += (
)

TEST_RUNNER = 'djangobase.settings.tests.ReusableRunner'

with open(os.path.normpath(os.path.join(SITE_ROOT, "ansible/env_vars/secure.yml")), "rb") as f:
    secrets = yaml.load(f)

    # Do loading of application secrets here

STATIC_URL ='/static/'
MEDIA_URL='/media/'