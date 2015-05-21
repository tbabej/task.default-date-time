Taskwarrior Default Date Time Tracking Hook
-------------------------------------------

This is a pair of hooks for TaskWarrior (http://www.taskwarrior.org),
which allow you to set a different time when specifying due time
using only dates.


Install
-------

Note: This hook has been rewritten to leverage taskpirate, for greater hook efficiency.
Please see https://github.com/tbabej/taskpirate for instructions. Don't worry, it's straightforward.

```
git clone https://github.com/tbabej/taskwarrior-default-date-time-hook.git ~/.task/hooks/default-time
```

This hook leverages tasklib, so you need to install that too:

```
pip --user install tasklib
```

You’ll also need to install the [taskw library](https://github.com/ralphbean/taskw/tree/develop), hich allows us to read the configuration file:

```
git clone -b develop https://github.com/ralphbean/taskw.git
cp -r taskw/taskw ~/.local/lib/python2.7/site-packages/
```

Configuration
-------------

Configure the timezone and default time with ```task config```:

```
task config default.time 22:00
task config default.timezone Europe/Madrid

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
