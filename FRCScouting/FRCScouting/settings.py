"""
Django settings for FRCScouting project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=x6gg3@#2mio1alr8s26$x*&9^s(%gn4c8g^7=ek1=73_&x)om'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Blog.apps.BlogConfig',
    'TheBlueAlliance.apps.TheblueallianceConfig',
    'ContentPages.apps.ContentpagesConfig',
    'Scouting.apps.ScoutingConfig',
    'Accounts.apps.AccountsConfig',
    'Contact.apps.ContactConfig',
    'eggs.apps.EggsConfig',
    'FIRSTEventsAPI.apps.FirsteventsapiConfig',
    'Events',
    'Teams',
    'Games.Stronghold',
    'Games.Steamworks',
    'Games.Powerup',
    'Games.DeepSpace',
    'Games.Rise',
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

AUTH_USER_MODEL = 'Accounts.User'

ROOT_URLCONF = 'FRCScouting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'FRCScouting/templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FRCScouting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'frcscouting',
        'USER': 'aaronspindler',
        'PASSWORD' : 'placehoulderpassword',
        'HOST' : 'localhost',
        'PORT' : '',
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'FRCScouting/static')]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


THE_BLUE_ALLIANCE_KEY = 'p8MD1dJfS2xOHD6cX7MIIW1mcFw1GWHuBKlUq9foxjt1Fp4f17B9PoYVreTBLC7a'
FMS_API_USER = 'sampleuser'
FMS_API_KEY = '7eaa6338-a097-4221-ac04-b6120fcc4d49'

#Only thing it can do is lookup maps, so don't event try
GOOGLE_MAPS_KEY = 'AIzaSyDwLAsY6lVwtiAwAHZQP7jGtoRtt0WyHEY'


if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testingdb'
    }
else:
    try:
        from .local_settings import *
    except ImportError:
        pass
