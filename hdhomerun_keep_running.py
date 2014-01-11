#!/usr/bin/python
### KEEP HDHOMERUN RECORDER RUNNING PUT IN CRON 5 minutes
import os

find = 'hdhomerun_recorder'
start = '/storage/etc/hdhomerun_recorder/start.sh &'

f = os.popen('ps ax | grep -v grep | grep "' + find + '"')
out = f.read()
if not find in out:
  print 'Running: ' + start
  os.system(start)

