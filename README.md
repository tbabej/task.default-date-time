Taskwarrior Default Date Time Tracking Hook
-------------------------------------------

This is a pair of hooks for TaskWarrior (http://www.taskwarrior.org),
which allow you to set a different time when specifying due time
using only dates.


Install
-------

```
git clone https://github.com/tbabej/taskwarrior-default-date-time-hook.git
cp taskwarrior-default-date-time-hook/on-* ~/.task/hooks/
```

This hook leverages tasklib, so you need to install that too:

```
sudo pip install --force git+git://github.com/tbabej/tasklib@localized_timestamps
```

Note: temporarily use my localized_timestamps branch, the currently released
version of the tasklib does not have all the goodies :)

Configuration
-------------

Edit both scripts and set ```LOCAL_TZ``` to your timezone and your desired
local ```DEFAULT_TIME```. For EST, default task date time of 21:30, it should look
as follows::

```
LOCALTZ = pytz.timezone('EST')  # Your timezone
DEFAULT_TIME = time(21,30,0)  # Your wanted default time
```

Example of usage
----------------

Add a task that has specified due time, but only as a date.

```
$ task add test due:today
Created task 4.
Default due time has been set.
```

We can see the message is outputted to notify us that
custom default due time has been used. Indeed, if we check:

```
$ task 4 info

Name          Value                                     
ID            4
Description   test                                      
Status        Pending
Entered       2015-01-08 07:17:26 (44 seconds)          
Due           2015-01-08 22:00:00
Last modified 2015-01-08 07:17:26 (44 seconds)          
UUID          86d1b114-6550-4213-82dd-d42a05828288
Urgency       8.672                                     
                               due 0.723  *   12 =  8.67
```

We can see this task has due time of 22:00.
