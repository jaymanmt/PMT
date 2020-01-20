"""
Django settings for PMT project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["olecrafit.herokuapp.com","sgmuaythai.herokuapp.com","www.sgmuaythai.org", "6d36a1919bc843a498ae983b9dca4512.vfs.cloud9.us-east-1.amazonaws.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'storages',
    'accounts',
    'shop',
    'basket',
    'payment',
    'administrator',
    'story'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PMT.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'basket.context_processor.basketcount'
            ],
        },
    },
]

WSGI_APPLICATION = 'PMT.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# for development activate sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'accounts.MyUser' 

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

LOGIN_REDIRECT_URL = '/accounts/login'
LOGIN_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = '/accounts/logout'

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY=os.environ["MAILGUN_ACCESS_KEY"]
MAILGUN_SERVER_NAME=os.environ["MAILGUN_SERVER_NAME"]
DEFAULT_FROM_EMAIL="no-reply@mail.sgmuaythai.org"
FROM_EMAIL="no-reply@mail.sgmuaythai.org"


STRIPE_PUBLISHABLE_KEY = os.environ["STRIPE_PUBLISHABLE_KEY"]
STRIPE_SECRET_KEY = os.environ["STRIPE_SECRET_KEY"]

AWS_S3_OBJECT_PARAMETERS={
    'Expires':'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl':'max-age=946800'
}

AWS_STORAGE_BUCKET_NAME="jtxh-files"
AWS_S3_REGION_NAME="ap-southeast-1"
AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY=os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_S3_CUSTOM_DOMAIN="{}.s3.amazonaws.com".format(AWS_STORAGE_BUCKET_NAME)

STATICFILES_STORAGE="custom_storages.StaticStorage"

STATICFILES_LOCATION="static"
DEFAULT_FILE_STORAGE='custom_storages.MediaStorage'

MEDIAFILES_LOCATION="media"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

DATABASES = {'default': dj_database_url.parse(os.environ['PG_HEROKU'])}

MAPBOX_ACCESS_TOKEN=os.environ["MAPBOX_ACCESS_TOKEN"]

COMPANY_EMAIL=os.environ["COMPANY_EMAIL"]