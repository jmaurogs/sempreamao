import os, sys
sys.path.append('/home/sempreamao/apps_wsgi')
sys.path.append('/home/sempreamao/apps_wsgi/sempreamao')
os.environ['PYTHON_EGG_CACHE'] = '/home/sempreamao/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'sempreamao.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
