#!/usr/bin/python
from datetime import time
from tasklib.task import Task, local_zone
from taskw import TaskWarrior

config = TaskWarrior.load_config()
if ('time' in config["default"]):
    DEFAULT_TIME = datetime.strptime(config['default']['time'], u'%H:%M').time()
else:
    DEFAULT_TIME = time(22,0,0)  # Your wanted default time

def is_local_midnight(timestamp):
    return timestamp.astimezone(local_zone).time() == time(0,0,0)

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
