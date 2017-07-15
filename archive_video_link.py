# @author Jerry He
# @desc this script works in the Pythonista app in iOS
# @purpose gets a video link from clipboard and inserts into a database
__author__ = 'jerryxhe'

import clipboard
from sql import psqlClient

link = clipboard.get()

print link

m = psqlClient()
m.execute("INSERT INTO eduvideo(source, created_on) VALUES ('%s', NOW())" % link)
