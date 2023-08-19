"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import secrets
from pathlib import Path
import dj_database_url
from decouple import config
import boto3
import django_heroku
from storages.backends.s3boto3 import S3Boto3Storage

'''
#import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.



# Before using your Heroku app in production, make sure to review Django's deployment checklist:
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Django requires a unique secret key for each Django app, that is used by several of its
# security features. To simplify initial setup (without hardcoding the secret in the source
# code) we set this to a random value every time the app starts. However, this will mean many
# Django features break whenever an app restarts (for example, sessions will be logged out).
# In your production Heroku apps you should set the `DJANGO_SECRET_KEY` config var explicitly.
# Make sure to use a long unique value, like you would for a password. See:
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY
# https://devcenter.heroku.com/articles/config-vars
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(nbytes=64),
)

# The `DYNO` env var is set on Heroku CI, but it's not a real Heroku app, so we have to
# also explicitly exclude CI:
# https://devcenter.heroku.com/articles/heroku-ci#immutable-environment-variables
IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

# SECURITY WARNING: don't run with debug turned on in production!
if not IS_HEROKU_APP:
    DEBUG = True

# On Heroku, it's safe to use a wildcard for `ALLOWED_HOSTS``, since the Heroku router performs
# validation of the Host header in the incoming HTTP request. On other platforms you may need
# to list the expected hostnames explicitly to prevent HTTP Host header attacks. See:
# https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-ALLOWED_HOSTS
if IS_HEROKU_APP:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1']
'''

BASE_DIR = Path(__file__).resolve().parent.parent
print("base dir: ", str(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u3%w(irr39z7$yup#39=%-x@9w90v8kw=xdct&@8g3d-frm9c-"
#SECRET_KEY = os.environ.get('SECRET_KEY')
#LINE ABOVE COMMENDED OUT FOR SECURITY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "lanternDie",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates" ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3v7e3sb9psees',
        'USER': 'dloedpbabkbqtk',
        'PASSWORD': 'bf40188e9c2fcdf6a82aca3bbf6da256292dbc7944f9645568f37d448e2f2f25',
        'HOST': 'ec2-52-21-61-131.compute-1.amazonaws.com',
        'PORT':  '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/' #setting the base path for all images

'''
#Configuring Bucketeer for AWS S3 file management
AWS_ACCESS_KEY_ID = os.environ.get('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('BUCKETEER_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKETEER_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('BUCKETEER_AWS_REGION')
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = os.environ.get('S3_SIGNATURE_VERSION', default='s3v4')
AWS_S3_ENDPOINT_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

STATIC_DEFAULT_ACL = 'public-read'
STATIC_LOCATION = 'static'
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'storage_backends.StaticStorage'

PUBLIC_MEDIA_DEFAULT_ACL = 'public-read'
PUBLIC_MEDIA_LOCATION = 'media/public'

MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'storage_backends.PublicMediaStorage'

#only currently using the public class but this could be useful later
PRIVATE_MEDIA_DEFAULT_ACL = 'private'
PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'storage_backends.PrivateMediaStorage'


#second attempt at above

# Retrieve AWS credentials from environment variables
#aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
#aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
#aws_bucket_name = os.environ.get("AWS_STORAGE_BUCKET_NAME")
aws_access_key_id = 'AKIASGSDA34MAY223WPL'
aws_secret_access_key = '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'
aws_bucket_name = 'lanterndi3-heroku'

print(type(aws_bucket_name))
print("bucket name: ", aws_bucket_name)

# Initialize the S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Define the local file path and S3 object key
local_file_path = "lanternflyTest.jpeg"
s3_object_key = "lanterndi3-heroku/lanternflyTest.jpeg"

# Upload the file to S3
with open(local_file_path, "rb") as file:
    s3_client.upload_fileobj(file, aws_bucket_name, s3_object_key)
'''

#####################

# Configure Amazon S3 settings
AWS_ACCESS_KEY_ID = 'AKIASGSDA34MAY223WPL'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'lanterndi3-heroku'
AWS_DEFAULT_ACL = 'public-read'
AWS_QUERYSTRING_AUTH = False

# Use Amazon S3 for static and media files
DEFAULT_FILE_STORAGE = 'lanternDie.storage_backends.MediaStorage' #MIGHT NEED tO CHANGE TO BACKEND OR SOMETHING OF THE LIKES

# Configure Django-Heroku
django_heroku.settings(locals())

# Use the following storage backend for media files
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False  # Set this to True if you want to overwrite files


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000'
]

LOGIN_REDIRECT_URL = "/" #redirecting to the homepage
LOGOUT_REDIRECT_URL = "/"

#django_heroku.settings(locals())

# Heroku configuration
django_heroku.settings(locals())
