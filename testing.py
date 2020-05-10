import os
from mysite import settings
print(os.path.dirname(os.path.abspath(__file__)))
print(settings.INSTALLED_APPS[6:])
applist = settings.INSTALLED_APPS[6:]
for a in applist:
    print(a.split('.')[0])
    print(type(a.split('.')[0]))