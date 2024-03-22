import os, inspect
import django_dyn_dt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '79$g*#82qs_rl%3vmdand$g6#n%u9#w6c6$(-np%p@p3a2rhu!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'crispy_forms',
    'crispy_bootstrap5',
    'newdata',
    'matchday',
    'django_dyn_dt',
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

ROOT_URLCONF = 'acwr.urls'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TEMPLATE_DIR_DATATB = os.path.join(BASE_DIR, "django_dyn_dt/templates") # <-- NEW App

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),TEMPLATE_DIR_DATATB],
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

WSGI_APPLICATION = 'acwr.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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


LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DYN_DB_PKG_ROOT = os.path.dirname( inspect.getfile( django_dyn_dt ) ) # <-- NEW App

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),
                    os.path.join(DYN_DB_PKG_ROOT, "templates/static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

CKEDITOR_JQUERY_URL = os.path.join(STATIC_URL, 'js/jquery.min.js')

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
    },
}

DYNAMIC_DATATB = {
    # SLUG -> Import_PATH
    'trainingData': "newdata.models.TrainingData",
}