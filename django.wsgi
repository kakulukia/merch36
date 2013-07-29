import os
import sys

sys.path.append('/home/andy/projects/merch36/')
sys.path.append('/home/andy/.virtualenvs/merch36/lib/python2.7/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'merch36.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
