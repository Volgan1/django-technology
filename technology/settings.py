# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

import os
import sys
from utils.misc import get_media_svn_revision, get_git_changeset

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

EXTERNAL_LIBS_PATH = os.path.join(BASE_DIR, "externals", "libs")
EXTERNAL_APPS_PATH = os.path.join(BASE_DIR, "externals", "apps")
sys.path = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path

MEDIA_ROOT = os.path.join(BASE_DIR, "technology", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "technology", "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "technology", "site_static"),)

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)
FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, "technology", "tmp")

STATIC_URL = "/static/%s/" % get_media_svn_revision(BASE_DIR)
STATIC_URL = "/static/%s/" % get_git_changeset(BASE_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f@d7m158v^g1dw(2mwb4h@7x_)+0$i08eej+f2%+8+(k@l7wwb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'techsite',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'technology.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "technology", "templates"),],
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

WSGI_APPLICATION = 'technology.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'

try:
    exec(open(os.path.join(os.path.dirname(__file__), "loc_settings.py")).read())
except IOError:
    pass
