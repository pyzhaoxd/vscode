
import os
import sys

import django


if __name__ == '__main__':
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetworkAutomation.settings')
   django.setup()
   from cmdb.models import Interface,Device
   dev = Device.objects.first()
   Interface(name='eth1/2',desc='ceshi',device=dev).save()

