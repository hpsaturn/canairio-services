"""
WSGI config for api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('../../') / '.env'
load_dotenv(dotenv_path=env_path)

if os.getenv('DJANGO_SETTINGS_MODULE') is not None:
    DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')
else:
    DJANGO_SETTINGS_MODULE = 'api.settings.prod'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

application = get_wsgi_application()
