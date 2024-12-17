import os
from environs import Env


env = Env()
env.read_env()

engine = env('ENGINE')
host = env('HOST')
port = env('PORT')
name = env('NAME')
guard = env('GUARD')
password_db = env('PASSWORD_DB')

secret_key = env('SECRET_KEY')
debug = env.bool('DEBUG', default=False)


DATABASES = {
    'default': {
        'ENGINE': engine,
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': guard,
        'PASSWORD': password_db,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = debug

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
