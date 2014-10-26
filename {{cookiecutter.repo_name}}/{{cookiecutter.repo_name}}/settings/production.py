from .base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{cookiecutter.repo_name}}',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

if 'CHANGE THIS' in SECRET_KEY:
    raise Exception('You must change settings.SECRET_KEY')

