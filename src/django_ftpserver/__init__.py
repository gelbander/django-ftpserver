__version__ = '0.3.2'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not hasattr(settings, 'FTPSERVER_ROOT'):
    raise ImproperlyConfigured('FTPSERVER_ROOT is not set.')
