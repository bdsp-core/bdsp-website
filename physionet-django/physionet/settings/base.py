"""
Django settings for physionet project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from decouple import config

import logging.config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ckeditor',
    # 'django_cron',
    'background_task',

    'user',
    'project',
    'console',
    'export',
    'notification',
    'search',
    'lightwave',
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

CRON_CLASSES = [
    "physionet.cron.RemoveUnverifiedEmails",
    "physionet.cron.RemoveOutstandingInvites",
]

ROOT_URLCONF = 'physionet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'physionet.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'user.validators.ComplexityValidator',
    },
]

AUTHENTICATION_BACKENDS = ['user.models.DualAuthModelBackend']

AUTH_USER_MODEL = 'user.User'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/projects/'

LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# Google Storge service account credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, 'PhysioNet-Data-credentials.json')

# Google G suite Groups service account and Private Key file
SERVICE_ACCOUNT_EMAIL = 'gcp-physionet-groups@physionet-data.iam.gserviceaccount.com'

SERVICE_ACCOUNT_PKCS12_FILE_PATH = os.path.join(BASE_DIR, 'PhysioNet-Data-credentials.p12')

GCP_DELEGATION_EMAIL = config('GCP_DELEGATION_EMAIL')
GCP_SECRET_KEY = config('GCP_SECRET_KEY')

# Header tags for the AWS lambda function that grants access to S3 storage
AWS_HEADER_KEY = config('AWS_KEY')
AWS_HEADER_VALUE = config('AWS_VALUE')
AWS_HEADER_KEY2 = config('AWS_KEY2')
AWS_HEADER_VALUE2 = config('AWS_VALUE2')
AWS_CLOUD_FORMATION = config('AWS_CLOUD_FORMATION')

# List of permitted HTML tags and attributes for rich text fields.
# The 'default' configuration permits all of the tags below.  Other
# configurations may be added that permit different sets of tags.

# Attributes that can be added to any HTML tag
_generic_attributes = ['lang', 'title']

# Inline/phrasing content
_inline_tags = {
    'a':      {'attributes': ['href']},
    'abbr':   True,
    'b':      True,
    'bdi':    True,
    'cite':   True,
    'code':   True,
    'dfn':    True,
    'em':     True,
    'i':      True,
    'kbd':    True,
    'q':      True,
    'rb':     True,
    'rp':     True,
    'rt':     True,
    'rtc':    True,
    'ruby':   True,
    's':      True,
    'samp':   True,
    'span':   True,
    'strong': True,
    'sub':    True,
    'sup':    True,
    'time':   True,
    'u':      True,
    'var':    True,
    'wbr':    True,
    'img':    {'attributes': ['alt', 'src', 'height', 'width']},
}
# Block/flow content
_block_tags = {
    # Paragraphs, lists, quotes, line breaks
    'blockquote': True,
    'br':         True,
    'dd':         True,
    'div':        True,
    'dl':         True,
    'dt':         True,
    'li':         {'attributes': ['value']},
    'ol':         {'attributes': ['start', 'type']},
    'p':          True,
    'pre':        True,
    'ul':         True,

    # Tables
    'caption':    True,
    'col':        {'attributes': ['span']},
    'colgroup':   {'attributes': ['span']},
    'table':      {'attributes': ['width']},
    'tbody':      True,
    'td':         {'attributes': ['colspan', 'headers', 'rowspan', 'style'],
                   'styles': ['text-align']},
    'tfoot':      True,
    'th':         {'attributes': ['abbr', 'colspan', 'headers', 'rowspan',
                                  'scope', 'sorted', 'style'],
                   'styles': ['text-align']},
    'thead':      True,
    'tr':         True,
}
# Math content (inline or block)
_math_tags = {
    'math':          {'attributes': ['alttext', 'display']},
    'annotation':    {'attributes': ['encoding']},
    'semantics':     True,

    'maligngroup':   {'attributes': ['groupalign']},
    'malignmark':    {'attributes': ['edge']},
    'menclose':      {'attributes': ['notation']},
    'merror':        True,
    'mfenced':       {'attributes': ['close', 'open', 'separators']},
    'mfrac':         {'attributes': [
        'bevelled', 'numalign', 'denomalign', 'linethickness']},
    'mi':            {'attributes': ['class', 'mathsize', 'mathvariant']},
    'mlabeledtr':    {'attributes': ['rowalign', 'columnalign', 'groupalign']},
    'mmultiscripts': True,
    'mn':            {'attributes': ['class', 'mathsize', 'mathvariant']},
    'mo':            {'attributes': [
        'class', 'accent', 'fence', 'form', 'largeop', 'linebreak',
        'linebreakmultchar', 'linebreakstyle', 'lspace', 'mathsize',
        'mathvariant', 'maxsize', 'minsize', 'movablelimits', 'rspace',
        'separator', 'stretchy', 'symmetric']},
    'mover':         {'attributes': ['accent', 'align']},
    'mpadded':       {'attributes': [
        'depth', 'height', 'lspace', 'voffset', 'width']},
    'mphantom':      True,
    'mprescripts':   True,
    'mroot':         True,
    'mrow':          {'attributes': ['class']},
    'ms':            {'attributes': ['lquote', 'rquote']},
    'mspace':        {'attributes': ['width', 'height', 'depth', 'linebreak']},
    'msqrt':         True,
    'mstyle':        {'attributes': [
        'decimalpoint', 'displaystyle', 'infixlinebreakstyle', 'mathsize',
        'mathvariant', 'scriptlevel', 'scriptsizemultiplier']},
    'msub':          True,
    'msubsup':       True,
    'msup':          True,
    'mtable':        {'attributes': [
        'align', 'alignmentscope', 'columnalign', 'columnlines',
        'columnspacing', 'columnwidth', 'displaystyle', 'equalcolumns',
        'equalrows', 'frame', 'groupalign', 'rowalign', 'rowlines',
        'rowspacing', 'side', 'width']},
    'mtd':           {'attributes': [
        'rowspan', 'columnspan', 'rowalign', 'columnalign', 'groupalign']},
    'mtext':         {'attributes': ['class', 'mathsize', 'mathvariant']},
    'mtr':           {'attributes': ['rowalign', 'columnalign', 'groupalign']},
    'munder':        {'attributes': ['accentunder', 'align']},
    'munderover':    {'attributes': ['accent', 'accentunder', 'align']},
    'none':          True,
}
# Classes used by MathJax (see toMathMLclass() in extensions/toMathML.js)
_math_classes = [
    'MJX-TeXAtom-ORD', 'MJX-TeXAtom-OP', 'MJX-TeXAtom-BIN', 'MJX-TeXAtom-REL',
    'MJX-TeXAtom-OPEN', 'MJX-TeXAtom-CLOSE', 'MJX-TeXAtom-PUNCT',
    'MJX-TeXAtom-INNER', 'MJX-TeXAtom-VCENTER',
    'MJX-fixedlimits', 'MJX-variant',
    'MJX-tex-caligraphic', 'MJX-tex-caligraphic-bold', 'MJX-tex-oldstyle',
    'MJX-tex-oldstyle-bold', 'MJX-tex-mathit',
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format'],
            ['Bold', 'Italic', 'Underline','Blockquote'],
            ['NumberedList', 'BulletedList'],
            ['InlineEquation', 'BlockEquation', 'CodeSnippet', 'Table'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'removeDialogTabs': 'link:advanced',
        'disableNativeSpellChecker': False,
        'width': '100%',
        'format_tags': 'p;h3',
        'extraPlugins': 'codesnippet,pnmathml',
        'allowedContent': {
            **_inline_tags,
            **_block_tags,
            **_math_tags,
            'h3': True,
            'h4': True,
            'h5': True,
            'h6': True,
            '*': {'attributes': _generic_attributes,
                  'classes': _math_classes},
        },
        'mathJaxLib': ('/static/mathjax/MathJax.js'
                       '?config=TeX-AMS-MML_HTMLorMML-full'),
    }

}

LOGGING_CONFIG = None
LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)-15s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'Custom_Logging': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/tmp/physionet.log',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }, 
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'user': {
            'level': 'INFO',
            'handlers': ['Custom_Logging'],
            'propagate': False,
        },
       'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'physionet.error': {
            'handlers': ['console', 'mail_admins', 'Custom_Logging'],
            'level': 'ERROR',
        }
    },
})
