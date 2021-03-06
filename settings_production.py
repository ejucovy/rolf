from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/rolf/rolf/templates",
)

MEDIA_ROOT = '/var/www/rolf/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/rolf/rolf/sitemedia')
)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except ImportError:
    pass

try:
    INSTALLED_APPS += LOCAL_INSTALLED_APPS
except:
    pass
