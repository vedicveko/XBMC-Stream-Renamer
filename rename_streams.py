#!/usr/bin/python

import xmltv
from pprint import pprint
import os, re, shutil, datetime

#import sys # TESTING

# Our current time and the max into the future we care to look
now = int(datetime.datetime.now().strftime("%Y%m%d%H%M00"))
too_far = now + 40000 

# Our TV data from mc2xml
filename = '/storage/dean/mc2xml-local/xmltv.xml'

# Our base stream files. These are named after the call sign of the station they represent
stream_defaults = '/storage/dean/Streams-default'
# Where to put our streams when done with them
stream_dir = '/storage/Streams'

# Holds our formatted data about the channels we care about
data = {} 

# Channels we received 
mychannels = []
for stream in os.listdir(stream_defaults):
  if '.strm' in stream:
    mychannels.append(stream.replace('.strm', ''))

 

# Loop through our xmltv data and get information on our channels
channels = xmltv.read_channels(open(filename, 'r'))
for c in channels:
  callsign = c['display-name'][2][0]
  if callsign in mychannels:
    id = c['id']

    display_name = ''

    if(len(c['display-name']) > 4):
      display_name = c['display-name'][4][0]
    else:
      display_name = c['display-name'][3][0]
  
    display_name = display_name.replace(' Low Power', '')
    display_name = display_name.replace(' Affiliate', '')

    data[id] = {}
    data[id]['id'] = id 
    data[id]['callsign'] = callsign
    data[id]['network'] = display_name

# Print programmes
programs = xmltv.read_programmes(open(filename, 'r'))

next = 0
for p in programs: 
  t = p['channel']
  if(t in data):

    start = int(str(p['start']).replace(' -0600', '')) 
    end = int(str(p['stop']).replace(' -0600', ''))

    if(next == 1):
      data[t]['next'] = p['title'][0][0]
      next = 0
      callsign = data[t]['callsign']
      data[callsign] = {}
      data[callsign] = data[t] 

    if(now > start and now < end):
      data[t]['now'] = p['title'][0][0]
      next = 1
      
prefix = 'LOC-'

if(len(mychannels)):
  os.system('rm ' + stream_dir + '/' + prefix + '*.strm')

for callsign in mychannels:
  if(callsign in data): 
    playing = data[callsign]['now'] + ' -N- ' + data[callsign]['next']
    playing = re.sub('[^\w\-_\. ]', '', playing)
    new_name = prefix + data[callsign]['network'] + ': ' + playing
  else:
    new_name = prefix + callsign + ': ?' 

#  print new_name
  shutil.copy(stream_defaults + '/' + callsign + '.strm', stream_dir + '/' + new_name + '.strm') 


