from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--(3awtoa46ow_b3zx1=kmv=6m&guj8y!3h+y1v)q#s@_(&1q5^"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    'tailwind',
    'theme',
    'django_browser_reload'
    
]

MIDDLEWARE += [
  "django_browser_reload.middleware.BrowserReloadMiddleware",
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "D:/Program Files/nodejs/npm.cmd" 

TAILWIND_CSS_PATH = 'css/main.css'

try:
    from .local import *
except ImportError:
    pass
