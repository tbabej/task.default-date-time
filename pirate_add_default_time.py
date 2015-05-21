#!/usr/bin/python
from datetime import time, datetime, timedelta
from taskw import TaskWarrior
from pytz import timezone, utc

CONFIG = TaskWarrior.load_config()
if 'timezone' in CONFIG['default']:
    DEFAULT_ZONE = timezone(CONFIG['default']['timezone'])
else:
    DEFAULT_ZONE = utc

if 'time' in CONFIG["default"]:
    DEFAULT_TIME = datetime.strptime(CONFIG['default']['time'], u'%H:%M').time()
else:
    DEFAULT_TIME = time(0, 0, 0, 0, DEFAULT_ZONE)

def is_local_midnight(timestamp):
    tmp = utc.localize(timestamp).astimezone(DEFAULT_ZONE)
    return tmp.time() == time(0, 0, 0)

def set_default_time(timestamp):
    return timestamp.astimezone(local_zone).replace(
        hour=DEFAULT_TIME.hour,
        minute=DEFAULT_TIME.minute,
        second=DEFAULT_TIME.second,
        )

def hook_default_time(task):
    if task['due'] and is_local_midnight(task['due']):
        task['due'] = set_default_time(task['due'])
        print "Default due time has been set."
