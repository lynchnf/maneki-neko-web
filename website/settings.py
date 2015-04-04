import os
import env_settings
gettext = lambda s: s
"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_settings.DEBUG

TEMPLATE_DEBUG = env_settings.TEMPLATE_DEBUG

ADMINS = env_settings.ADMINS

MANAGERS = env_settings.MANAGERS

ALLOWED_HOSTS = env_settings.ALLOWED_HOSTS


# Application definition

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import sys
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': u':memory:'
        }
    }
else:
    DATABASES = env_settings.DATABASES

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'website', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'website', 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
#    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
#    'djangocms_flash',
    'djangocms_googlemap',
#    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
#    'djangocms_teaser',
#    'djangocms_video',
    'easy_thumbnails',
    'filer',
    'cmsplugin_gallery',
    'reversion',
    'website',
    'analytics',
    'headtags',
    'navigation',
    'socialmedia',
    'staff'
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ('con-home.html', 'Convention home page'),
    ('con-other.html', 'Other Convention page'),
    ('con-full.html', 'Full Width Convention page'),
    ('corp.html', 'Sponsoring corporation page')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'meta': {
        'plugins': ['MetaTagPlugin']
    },
    'analytics': {
        'plugins': ['GoogleAnalyticsPlugin']
    },
    'images': {
        'plugins': ['PicturePlugin', 'CMSGalleryPlugin']
    },
    'social-links': {
        'plugins': ['SocialLinkPlugin']
    },
    'news': {
        'plugins': ['TextPlugin'],
        'text_only_plugins': ['LinkPlugin']
    },
    'footer-text': {
        'plugins': ['TextPlugin'],
        'text_only_plugins': ['LinkPlugin']
    },
    'footer-links': {
        'plugins': ['LinkPlugin']
    },                        
    'corporation-footer': {
        'plugins': ['TextPlugin'],
        'text_only_plugins': ['LinkPlugin']
    }                        
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

EMAIL_BACKEND = env_settings.EMAIL_BACKEND 
EMAIL_HOST = env_settings.EMAIL_HOST
EMAIL_HOST_USER = env_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = env_settings.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = env_settings.EMAIL_USE_TLS
EMAIL_PORT = env_settings.EMAIL_PORT
EMAIL_SUBJECT_PREFIX = '[WEBSITE ERROR] '
CONTACT_US_SUBJECT_PREFIX = '[Maneki Neko Con] '

LOGGING = env_settings.LOGGING