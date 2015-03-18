from django.conf.global_settings import MANAGERS
SECRET_KEY = '&d1#ne%8(2$rcu5wn9pibbmoud8g14j@@y$fi_%))@7upw&v7('

DEBUG = True

TEMPLATE_DEBUG = True

ADMINS = ()

MANAGERS = ()

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': u'mnwebdb',
        'HOST': u'localhost',
        'USER': u'mnwebuser',
        'PASSWORD': u'swordfish',
        'PORT': 3306
    }
}

# For production, EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# For development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 25

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'console_fmt': {
            'format': '%(levelname)-7s | %(name)s | %(message)s'
        },
        'file_fmt': {
            'format': '%(processName)s %(asctime)s | %(name)s | %(levelname)-7s | %(message)s'
        }                   
    },
    'handlers': {
        'console': {
            'formatter': 'console_fmt',
            'class': 'logging.StreamHandler'
        },
        'file': {
            'formatter': 'file_fmt',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'maneki-neko-web.log'
        }
    },
    'loggers': {
        'analytics': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
        'navigation': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
        'socialmedia': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
        'staff': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
        'website': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
# Everything else goes to the root logger.                
        '': {
            'level': 'INFO',
            'handlers': ['console','file']
        }
    }
}