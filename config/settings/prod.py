from .base import *

ALLOWED_HOSTS = ["*"]
env_file = str(PROJECT_ROOT.path('security/environ_prod.env'))
environ.Env.read_env(str(env_file))

DEBUG = env.bool('DEBUG_PROD')
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader',
     TEMPLATES[0]['OPTIONS']['loaders']),
]
SECRET_KEY = env('SECRET_KEY')


# DATABASES = {
#     'default': env.db("DATABASE_URL_PROD"),
# }
DATABASES = {
    'default': env.db("SQLITE_URL_LOCAL"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 10


# CACHES = {
#     'default': env.cache('REDIS_URL')
# }
#
# SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
# SESSION_CACHE_ALIAS = "default"

DJANGO_APPS = (
)

THIRD_PARTY_APPS = (
    'storages',
)
LOCAL_APPS = ()

INSTALLED_APPS += DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

ADMIN_URL = env('ADMIN_URL_PROD')

EMAIL_CONFIG = env.email_url('EMAIL_URL_PROD')
vars().update(EMAIL_CONFIG)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# if SITE_SCHEME == 'https':
SECURE_HSTS_SECONDS = env.int('DJANGO_SECURE_HSTS_SECONDS', default=60)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# --------------------AMAZON STORAGE----------------------------------

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
AWS_PRELOAD_METADATA = True

STATICFILES_LOCATION = 'static'
STATIC_URL = u"https://{0:s}/{1:s}/".format(AWS_S3_CUSTOM_DOMAIN,
                                            STATICFILES_LOCATION)
STATICFILES_STORAGE = 'core.custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = u"https://{0:s}/{1:s}/".format(AWS_S3_CUSTOM_DOMAIN,
                                           MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'core.custom_storages.MediaStorage'



# --------------------GOOGLE STORAGE----------------------------------

# GS_ACCESS_KEY_ID = env('GCLOUD_ACCESS_KEY_ID')
# GS_SECRET_ACCESS_KEY = env('GCLOUD_SECRET_ACCESS_KEY')
# GS_BUCKET_NAME = env('GCLOUD_STORAGE_BUCKET_NAME')
# GS_CUSTOM_DOMAIN = 'storage.googleapis.com/%s' % GS_BUCKET_NAME
#
#
# STATICFILES_LOCATION = 'static'
# STATIC_URL = "https://storage.googleapis.com/{0}/{1}/".format(
#     str(GS_BUCKET_NAME), str(STATICFILES_LOCATION)
# )
#
# STATICFILES_STORAGE = 'core.custom_storages.StaticStorage'
#
# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://storage.googleapis.com/{0}/{1}/".format(
#     str(GS_BUCKET_NAME), str(MEDIAFILES_LOCATION)
# )
# DEFAULT_FILE_STORAGE = 'core.custom_storages.MediaStorage'

