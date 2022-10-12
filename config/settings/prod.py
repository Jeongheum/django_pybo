# settings for production

# shell script (mysite.sh) for production setting
#!/bin/bash
# cd ~/projects/mysite
# export DJANGO_SETTINGS_MODULE=config.settings.prod
# . ~/venvs/mysite/bin/activate

from .base import *

ALLOWED_HOSTS = ['3.37.58.70']
STATIC_ROOT = BASE_DIR / 'pybo/static/'
STATICFILES_DIRS = []
DEBUG = False