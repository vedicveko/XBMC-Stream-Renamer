#!/usr/bin/python

### PROCESS VIDEOS PRODUCED BY hdhomerun_record

import sys, os, shutil

temp_dir = '/storage/recordings_temp'
store_dir = '/storage/recordings'

### NO ARG MEANS WE LOOK AT THE WHOLE TEMP DIR FOR FILES
if(len(sys.argv) == 1):

  for root, dirs, files in os.walk(temp_dir):
    path = root.split('/')
    for file in files:
#      if(os.path.isfile(root + '/' + file)):
#        print 'is a file'

    
      if '.ts' in file:
        print root + '/' + file
        print 'Video'
        os.system('/storage/dean/hdhomerun_process.py "' + root + '/' + file + '"')

  sys.exit()


### Our file name contains all of the information about the video we need
filename = sys.argv[1]
file = os.path.basename(filename)
showname = os.path.dirname(filename).replace('/storage/recordings_temp/', '')

new_file = showname + ' - ' + file
nfo_file = new_file.replace('.ts', '.nfo')
date = file.replace('.ts', '')
dates = date.split('-')
year = dates[0]
month = dates[1]
day = dates[2]

# Copy a thumbnails
nthumb = new_file.replace('.ts', '.tbn') 
shutil.copy('/storage/dean/thumbnails/' + showname.replace('.ts', ''), store_dir + '/' + showname + '/' + nthumb) 

#### GRAB AND FIX NFO TEMPLATE
with open ("/storage/dean/series_template.nfo", "r") as myfile:
    template = myfile.read()

template = template.replace('_TITLE_', showname + ' ' + date)
template = template.replace('_DATE_', date)
template = template.replace('_YEAR_', year)
template = template.replace('_MONTH_', month)
template = template.replace('_DAY_', day)

text_file = open(store_dir + '/' + showname + '/' + nfo_file, "w")
text_file.write(template)
text_file.close()

# Copy the video to the correct spot and update xbmc
os.rename(filename, store_dir + '/' + showname + '/' + new_file)

os.system('/usr/bin/xbmc-send -a "UpdateLibrary(video, ' + store_dir + '/' + showname + ')"')

