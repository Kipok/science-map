from .base import *


DEBUG = False
ALLOWED_HOSTS = ['science-map.igitman.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {'read_default_file': os.path.join(BASE_DIR, 'db.conf')},
        'HOST': 'localhost',
        'PORT': '',
    }
}
