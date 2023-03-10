
#####################################
########## Django settings ##########
#####################################
# See <https://docs.djangoproject.com/en/1.11/ref/settings/>
# for more info and help. If you are stuck, you can try Googling about
# Django - many of these settings below have external documentation about them.
#
# The settings listed here are of special interest in configuring the site.

# SECURITY WARNING: keep the secret key used in production secret!
# You may use <http://www.miniwebtool.com/django-secret-key-generator/>
# to generate this key.
SECRET_KEY = os.environ.get('SECRET_KEY', '')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '0') == '1'
HOST = os.environ.get('HOST', '')

# Uncomment and set to the domain names this site is intended to serve.
# You must do this once you set DEBUG to False.
ALLOWED_HOSTS = [HOST]

# Optional apps that DMOJ can make use of.
INSTALLED_APPS += ()

# Caching. You can use memcached or redis instead.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/cache/>
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
    }
}

# Your database credentials. Only MySQL is supported by DMOJ.
# Documentation: <https://docs.djangoproject.com/en/1.11/ref/databases/>
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', ''),
        'USER': os.environ.get('MYSQL_USER', ''),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', ''),
        'HOST': os.environ.get('MYSQL_HOST', 'db'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION',
        },
    }
}

# Sessions.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/http/sessions/>
#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Internationalization.
# Documentation: <https://docs.djangoproject.com/en/1.11/topics/i18n/>
LANGUAGE_CODE = 'en-ca'
DEFAULT_USER_TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_L10N = True
USE_TZ = True

## django-compressor settings, for speeding up page load times by minifying CSS and JavaScript files.
# Documentation: https://django-compressor.readthedocs.io/en/latest/
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)


#########################################
########## Email configuration ##########
#########################################
# See <https://docs.djangoproject.com/en/1.11/topics/email/#email-backends>
# for more documentation. You should follow the information there to define 
# your email settings.

# Use this if you are just testing.
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# The following block is included for your convenience, if you want 
# to use Gmail.
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = '<your account>@gmail.com'
#EMAIL_HOST_PASSWORD = '<your password>'
#EMAIL_PORT = 587

# To use Mailgun, uncomment this block.
# You will need to run `pip install django-mailgun` for to get `MailgunBackend`.
#EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
#MAILGUN_ACCESS_KEY = '<your Mailgun access key>'
#MAILGUN_SERVER_NAME = '<your Mailgun domain>'

# You can also use Sendgrid, with `pip install sendgrid-django`.
#EMAIL_BACKEND = 'sgbackend.SendGridBackend'
#SENDGRID_API_KEY = '<Your SendGrid API Key>'

# The DMOJ site is able to notify administrators of errors via email,
# if configured as shown below.

# A tuple of (name, email) pairs that specifies those who will be mailed
# when the server experiences an error when DEBUG = False.
ADMINS = ()

# The sender for the aforementioned emails.
SERVER_EMAIL = 'DMOJ: Modern Online Judge <errors@dmoj.ca>'


##################################################
########### Static files configuration. ##########
##################################################
# See <https://docs.djangoproject.com/en/1.11/howto/static-files/>.

# Change this to somewhere more permanent., especially if you are using a 
# webserver to serve the static files. This is the directory where all the 
# static files DMOJ uses will be collected to.
# You must configure your webserver to serve this directory as /static/ in production.
STATIC_ROOT = '/assets/static/'

# URL to access static files.
STATIC_URL = '/static/'

# Uncomment to use hashed filenames with the cache framework.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

############################################
########## DMOJ-specific settings ##########
############################################

## DMOJ site display settings.
SITE_NAME = 'DMOJ'
SITE_LONG_NAME = 'DMOJ: Modern Online Judge'
SITE_ADMIN_EMAIL = 'admin@example.com'
TERMS_OF_SERVICE_URL = None

## Bridge controls.
# The judge connection address and port; where the judges will connect to the site.
# You should change this to something your judges can actually connect to 
# (e.g., a port that is unused and unblocked by a firewall).
BRIDGED_JUDGE_ADDRESS = [('bridged', 9999)]

# The bridged daemon bind address and port to communicate with the site.
BRIDGED_DJANGO_ADDRESS = [('bridged', 9998)]

## DMOJ features.
# Set to True to enable full-text searching for problems.
ENABLE_FTS = True

# Set of email providers to ban when a user registers, e.g., {'throwawaymail.com'}.
BAD_MAIL_PROVIDERS = set()

## Event server.
# Uncomment to enable live updating.
EVENT_DAEMON_USE = True

# Uncomment this section to use websocket/daemon.js included in the site.
#EVENT_DAEMON_POST = '<ws:// URL to post to>'

# If you are using the defaults from the guide, it is this:
EVENT_DAEMON_POST = 'ws://wsevent:15101/'

# These are the publicly accessed interface configurations.
# They should match those used by the script.
EVENT_DAEMON_GET = 'ws://{host}/event/'.format(host=HOST)
EVENT_DAEMON_GET_SSL = 'wss://{host}/event/'.format(host=HOST)
EVENT_DAEMON_POLL = '/channels/'

# If you would like to use the AMQP-based event server from <https://github.com/DMOJ/event-server>,
# uncomment this section instead. This is more involved, and recommended to be done
# only after you have a working event server.
#EVENT_DAEMON_AMQP = '<amqp:// URL to connect to, including username and password>'
#EVENT_DAEMON_AMQP_EXCHANGE = '<AMQP exchange to use>'

## CDN control.
# Base URL for a copy of ace editor.
# Should contain ace.js, along with mode-*.js.
ACE_URL = '//cdnjs.cloudflare.com/ajax/libs/ace/1.2.3/'
JQUERY_JS = '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js'
SELECT2_JS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js'
SELECT2_CSS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css'

# A map of Earth in Equirectangular projection, for timezone selection.
# Please try not to hotlink this poor site.
TIMEZONE_MAP = 'http://naturalearth.springercarto.com/ne3_data/8192/textures/3_no_ice_clouds_8k.jpg'

## Camo (https://github.com/atmos/camo) usage.
#DMOJ_CAMO_URL = "<URL to your camo install>"
#DMOJ_CAMO_KEY = "<The CAMO_KEY environmental variable you used>"

# Domains to exclude from being camo'd.
#DMOJ_CAMO_EXCLUDE = ("https://dmoj.ml", "https://dmoj.ca")

# Set to True to use https when dealing with protocol-relative URLs.
# See <http://www.paulirish.com/2010/the-protocol-relative-url/> for what they are.
#DMOJ_CAMO_HTTPS = False

# HTTPS level. Affects <link rel='canonical'> elements generated.
# Set to 0 to make http URLs canonical.
# Set to 1 to make the currently used protocol canonical.
# Set to 2 to make https URLs canonical.
#DMOJ_HTTPS = 0

## PDF rendering settings.
# Directory to cache the PDF.
DMOJ_PDF_PROBLEM_CACHE = '/pdfcache'

# Path to use for nginx's X-Accel-Redirect feature.
# Should be an internal location mapped to the above directory.
DMOJ_PDF_PROBLEM_INTERNAL = '/pdfcache'


DMOJ_USER_DATA_DOWNLOAD = True
DMOJ_USER_DATA_CACHE = '/datacache'
DMOJ_USER_DATA_INTERNAL = '/datacache'

#############
## Mathoid ##
#############
# Documentation: https://github.com/wikimedia/mathoid
MATHOID_URL = 'http://mathoid:10044'
MATHOID_CACHE_ROOT = '/cache/mathoid/'
MATHOID_CACHE_URL = '//{host}/mathoid/'.format(host=HOST)

############
## Pdfoid ##
############

DMOJ_PDF_PDFOID_URL = 'http://pdfoid:8888'

############
## Texoid ##
############

TEXOID_URL = 'http://texoid:8888'
TEXOID_CACHE_ROOT = '/cache/texoid/'
TEXOID_CACHE_URL = '//{host}/texoid/'.format(host=HOST)

## ======== Logging Settings ========
# Documentation: https://docs.djangoproject.com/en/1.9/ref/settings/#logging
#                https://docs.python.org/2/library/logging.config.html#logging-config-dictschema
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'file',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

## ======== Integration Settings ========
## Python Social Auth
# Documentation: https://python-social-auth.readthedocs.io/en/latest/
# You can define these to enable authentication through the following services.
#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
#SOCIAL_AUTH_FACEBOOK_KEY = ''
#SOCIAL_AUTH_FACEBOOK_SECRET = ''
#SOCIAL_AUTH_GITHUB_SECURE_KEY = ''
#SOCIAL_AUTH_GITHUB_SECURE_SECRET = ''
#SOCIAL_AUTH_DROPBOX_OAUTH2_KEY = ''
#SOCIAL_AUTH_DROPBOX_OAUTH2_SECRET = ''

## ======== Custom Configuration ========
# You may add whatever django configuration you would like here.
# Do try to keep it separate so you can quickly patch in new settings.

# Uncomment if you're using HTTPS to ensure CSRF and session cookies are
# sent only with an HTTPS connection.
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True

REGISTRATION_OPEN = False
DMOJ_RATING_COLORS = True
X_FRAME_OPTIONS = 'DENY'

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

DMOJ_PROBLEM_DATA_ROOT = '/problems/'

DMOJ_RESOURCES = '/assets/resources/'

MEDIA_ROOT = '/media/'
MEDIA_URL = '/media/'
