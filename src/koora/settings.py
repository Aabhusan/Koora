"""
Django settings for koora project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ['SECRET_KEY']

JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 86400


DEBUG = os.environ['DEBUG'] == 'TRUE'

ADMIN_ENABLED = DEBUG

ALLOWED_HOSTS = ['*']


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_URL = '/auth/login/google-oauth2/'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['GOOGLE_OAUTH_CLIENT_ID']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['GOOGLE_OAUTH_CLIENT_SECRET']


CSRF_FAILURE_VIEW = 'koora.views.csrf_fail'

#Settings for Article Categories

KOORA_CATEGORIES = [
    ('AR', 'ART'),
    ('FD', 'FOOD'),
    ('GM', 'GAMES'),
    ('RN', 'RANDOM'),
    ('SC', 'SCIENCE'),
    ('TS', 'TVSERIES'),
    ('TG', 'TECHNOLOGY'),
    ('LT', 'LITERATURE'),
    ('PH', 'PHILOSOPHY'),
    ('MM', 'MUSIC&MOVIES'),
]

# Application definition

INSTALLED_APPS = [
    'boto3',
    'social_django',
    'django_social_share',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'articles.apps.ArticlesConfig',
    'user.apps.UserConfig',
    'comments.apps.CommentsConfig',
    'django.contrib.auth',
    'authentication.apps.AuthenticationConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'authentication.middlewares.AuthMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


if not DEBUG:  # adding after the security middleware
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


ROOT_URLCONF = 'koora.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'koora.context.interceptor'
            ],
        },
    },
]

WSGI_APPLICATION = 'koora.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ['PY_ENV'] == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.' + os.environ['DB_ENGINE'],
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USER'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ['DB_PORT'],
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [ os.path.join(BASE_DIR, "assets"), ]


# MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')


