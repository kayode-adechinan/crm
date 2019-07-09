from .base import *

DEBUG = True

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': ':memory:'
#    }
#}

#INSTALLED_APPS += [
#    'debug_toolbar',
#]

#MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'