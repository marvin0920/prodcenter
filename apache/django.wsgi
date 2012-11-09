
import os
import sys

#Calculate the path based on the location of the WSGI script.

app_path = '/home/marvin/Mousehouse/prodcenter/prodcenter'
sys.path.append(app_path)

#apache_configuration= os.path.dirname(__file__)
#project = os.path.dirname(apache_configuration)
#workspace = os.path.dirname(project)
#sys.path.append(workspace) 

sys.stdout = sys.stderr
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler() 
