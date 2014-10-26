from .base import *


ADMINS = (
    ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{cookiecutter.repo_name}}',
        'USER': '{{cookiecutter.username}}',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


ALLOWED_HOSTS = ['localhost', '127.0.0.1']
