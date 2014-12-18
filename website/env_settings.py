SECRET_KEY = '&d1#ne%8(2$rcu5wn9pibbmoud8g14j@@y$fi_%))@7upw&v7('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

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
            'filename': '/var/log/maneki-neko-con/website.log'
        }
    },
    'loggers': {
        'socialmedia': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
        'website': {
            'level': 'DEBUG',
            'handlers': ['console','file']
        },
# Everything else goes to the root logger.                
        'website': {
            'level': 'INFO',
            'handlers': ['console','file']
        }
    }
}