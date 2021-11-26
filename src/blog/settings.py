from pathlib import Path
import os
# import environ
from decouple import config
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG")

ALLOWED_HOSTS = config('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',

    'tinymce',
    'post',
    'marketing',
    'ckeditor',
    'crispy_forms',
    'accounts',
    'galerie',
    'tendances',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'galerie.context_processors.galerie_context',
                'post.context_processors.banner_context',
                'tendances.context_processors.context_tendance',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Database
DATABASES = {
    
    'default' : {

        'ENGINE'   : 'django.db.backends.mysql',
        'NAME'     : config('DATABASE_NAME'),
        'USER'     : config('DATABASE_USER') ,
        'PASSWORD' : config('DATABASE_PASSWORD') ,
        'HOST'     : config('DATABASE_HOST'),
        'PORT'     : config('DATABASE_PORT'),
    }
}


# DATABASES = {
#     'default' : (dj_database_url.config(default='postgres//postgres:admin@localhost/namory'))
# }


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]



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


LANGUAGE_CODE = config('LANGUAGE_CODE')

TIME_ZONE = config('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# VENDOR_PATH = os.path.dirname(BASE_DIR)
VENV_PATH =  os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
MEDIA_ROOT = os.path.join(VENV_PATH, 'media_root')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "fr_FR",  # To force a specific language instead of the Django current language.
}


SITE_ID = 1
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'account_login'

ACCOUNT_SIGNUP_REDIRECT_URL = "/accounts/login/"

# AUTH_USER_MODEL = 'accounts.Account'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',

}

# AUTH_USER_MODEL = 'accounts.Account'
# Configuration d'smtp server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True


# whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# {'login': 'accounts.forms.MyLoginForm'}
ACCOUNT_FORMS = {
    'login': 'accounts.forms.MyLoginForm',
    'reset_password': 'accounts.forms.MyCustomResetPasswordForm',
    'signup': 'accounts.forms.MySignupForm',
    'set_password': 'accounts.forms.PwdResetConfirmForm',    
    'add_email': 'accounts.forms.MyCustomAddEmailForm',
    'change_password': 'accounts.forms.MyCustomChangePasswordForm',
    'reset_password_from_key': 'accounts.forms.MyResetPasswordKeyForm',
    }
# ACCOUNT_FORMS = {'reset_password': 'accounts.forms.MyCustomResetPasswordForm'}
# MAILING SERVICE
MAILCHIMP_API_KEY = config('YOUR_API_KEY')
MAILCHIMP_DATA_CENTER = config('YOUR_LAST_3_CHARACTERS_OF_YOUR_API_KEY')
MAILCHIMP_EMAIL_LIST_ID = config('AUDIENCE_ID')
