import os
import sys
import platform
#путь к проекту, там где manage.py
sys.path.insert(0, '/home/c/cs44996/Amma/public_html/AMMA_PROJECT')
#путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/c/cs44996/Amma/public_html/AMMA_PROJECT/AMMA_PROJECT')
#путь к виртуальному окружению myenv
sys.path.insert(0, '/home/c/cs44996/Amma/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
#sys.path.insert(0, '/home/c/cs44996/Amma/venv/lib/python3.6/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "AMMA_PROJECT.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
