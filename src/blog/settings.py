from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-0s$=-)$*@r=64%&s_s3rp9k+gn#%e9r5jl%r3tznpr-v9n1cyi'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post.apps.PostConfig',
    'marketing.apps.MarketingConfig',
    'tinymce',
    'ckeditor',
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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TINYMCE_DEFAULT_CONFIG = {

#    'height': 360,

#    'width': 500,   

#    # 'height': 360,

#    # 'width': 600,

#    'cleanup_on_startup': True,

#    'custom_undo_redo_levels': 20,

#    'selector': 'textarea',

#    'theme': 'modern',

#    'plugins': '''

#    textcolor save link image media preview codesample contextmenu

#    table code lists fullscreen insertdatetime nonbreaking

#    contextmenu directionality searchreplace wordcount visualblocks

#    visualchars code fullscreen autolink lists charmap print hr

#    anchor pagebreak

#    ''',


#    'toolbar1': '''

#    fullscreen preview bold italic underline | fontselect,

#    fontsizeselect | forecolor backcolor | alignleft alignright |

#    aligncenter alignjustify | indent outdent | bullist numlist table |

#    | link image media | codesample |

  

#    ''',

#    'toolbar2': '''

#    visualblocks visualchars |

#    charmap hr pagebreak nonbreaking anchor | code |

#    ''',

#    'contextmenu': 'formats | link image',

#    'menubar': True,

#    'statusbar': True,

#    }
