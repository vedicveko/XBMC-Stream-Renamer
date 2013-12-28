#!/usr/bin/python
'''
    ustvnow XBMC Plugin
    Copyright (C) 2011 t0mm0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

20131227 - Modified by Dean Vaughan - http://deanvaughan.org
'''

'''
THIS GOES IN THE SAME DIRECTORY AS YOUR USTVNOW PLUGIN
'''

from resources.lib import Addon, ustvnow
import sys
import urllib
import os
import re

email = 'email@email' 
password = 'blahblah' 
ustv = ustvnow.Ustvnow(email, password)

stream_type = 'rtmp'
quality = '1'

channels = ustv.get_channels(int(quality), stream_type)

if(len(channels)):
  os.system("rm /storage/Streams/USTV-*")

for c in channels:
    title = c['now']['title']
    title = re.sub('[^\w\-_\. ]', '', title)
    title = title.replace(' amp ', ' and ')
    f = open('/storage/Streams/USTV-' + c['name'] + ': ' + title + '.strm', 'w')
    f.write(c['url'])
    f.close()
