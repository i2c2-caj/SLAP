"""
AUTHOR: COBY JOHNSON
PROJECT: SLAP (Sql-Lite wrApper in Python)
LAST UPDATE: 5/3/2014
VERSION: 0.0.1

== Adaptors ==
+ adapt_datetime(datetime.datetime.now()) => float (3/23/2014)

== Extractors ==
+ extract_datetime(float) => datetime.datetime.now() (3/23/2014)

TODO:
- [V 0.0.2]
    - Need to research converters (opposite of adapters)
    - Person/Name Class(first, middle, last)

- [V 0.0.3]
    - !! Encrypt all personal data put into db !!

"""

import sqlite3 as sql
import datetime
import time

#Create adaptor functions
def adapt_datetime(ts):
    return time.mktime(ts.timetuple())

def extract_datetime(f):
    return datetime.datetime.fromtimestamp(time.mktime(time.localtime(f)))

#Register Adapters
sql.register_adapter(datetime.datetime, adapt_datetime) 
