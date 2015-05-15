from djangobase.settings.prod import *

# The same settings as production, but no database password.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangobase_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

INSTALLED_APPS += (
)

TEST_RUNNER = 'djangobase.settings.tests.ReusableRunner'