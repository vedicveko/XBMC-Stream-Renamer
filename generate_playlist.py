#!/usr/bin/python

import os 

dir = '/storage/Streams'
out_file = dir + '/0 - Play All.pls'

c = 1
out = '' 

files = sorted(os.listdir(dir))

for file in files: 
  if '.strm' in file:
    with open (dir + '/' + file, "r") as stream_file:
      url = stream_file.read().replace('\n', '')
      out = out + "File" + str(c) + "=" + url + "\n"
      out = out + "Title" + str(c) + "=" + file.replace('.strm', '') + "\n"
      c = c + 1
c = c - 1
out = "[playlist]\nNumberOfEntries=" + str(c) + "\n" + out

f = open(out_file, 'w')
f.write(out)
f.close()
