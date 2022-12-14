"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ

# djanog-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG", default=False)

#SECURE_SSL_REDIRECT = env("DJANGO_SECURE_SSL_REDIRECT", default=True)

# 2592000 = one month in seconds
#SECURE_HSTS_SECONDS = env("DJANGO_SECURE_HSTS_SECONDS", default=2592000)

#SECURE_HSTS_INCLUDE_SUBDOMAINS = env("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)

#SECURE_HSTS_PRELOAD = env("DJANGO_SECURE_HSTS_PRELOAD", default=True)

#SESSION_COOKIE_SECURE = env("DJANGO_SESSION_COOKIE_SECURE", default=True)

#CSRF_COOKIE_SECURE = env("DJANGO_CSRF_COOKIE_SECURE", default=True)

ALLOWED_HOSTS = [env("DJANGO_HOSTS")]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'debug_toolbar',

    # local apps
    'home',
    'accounts',
    'books',
]

# django crispy forms setting
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-allauth config
SITE_ID = 1

# default redirects
LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

# account logout redirect overrides logout redirect url
ACCOUNT_LOGOUT_REDIRECT = 'home'

# toggle the remember me option for log in
ACCOUNT_SESSION_REMEMBER = True

# toggle repeat password option for sign up
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_UNIQUE_EMAIL = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

DEFAULT_FROM_EMAIL = 'django_development@django_development.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

"""
FOLLOWING TO BE USED WHEN SMTP EMAIL AVAILABLE

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_PORT = env("DJANGO_EMAIL_PORT")
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS")
"""

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # default looks for templates in each app
        # 'DIRS': [],
        # switched to centralised templates folder django will still look in each app
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

"""DEFAULT DATABASE sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DJANGO_DATABASE_NAME"),
        'USER': env("DJANGO_DATABASE_USER"),
        'PASSWORD': env("DJANGO_DATABASE_PASSWORD"),
        'HOST': env("DJANGO_DATABASE_HOST"),
        'PORT': env("DJANGO_DATABASE_PORT")
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# defines location in local development
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)

# defines location for production
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

# though implicitly set recommended to explicitly set it
STATICFILES_FINDERS = [
    # uses STATICFILES_DIR setting
    "django.contrib.staticfiles.finders.FileSystemFinder",
    # search for any directory named static with an app
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT = str(BASE_DIR.joinpath('media'))

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
