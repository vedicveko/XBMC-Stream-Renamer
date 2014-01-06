#!/usr/bin/python

import os

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("/storage/recordings"):
    path = root.split('/')
    for file in files:
        if '.ts' in file:
            print root + '/' + file
            print 'Video'
