from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackEnd'
