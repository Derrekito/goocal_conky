#!/usr/bin/python

__author__ = 'api.user_name@gmail.com'

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree

import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time

import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar

from datetime import date 

# Date parameters
today = date.today()
start_date = '%s'%(today)
month = today.month
if today.month <10:
  month = '0%s'%(today.month)
twodays = today.day+2
if twodays < 10:
  twodays = "0%s"%twodays
end_date = '%s-%s-%s'%(today.year,month,twodays)


def DateRangeQuery(calendar_service, start_date, end_date):
  query.start_min = start_date
  query.start_max = end_date
  feed = calendar_service.CalendarQuery(query)

  for i, an_event in enumerate(feed.entry):
    event_date = an_event.when[0].start_time[0:10]
    time_start = an_event.when[0].start_time[11:16]
    time_end = an_event.when[0].end_time[11:16]
    print '%s: %s' % (event_date, an_event.title.text,)
    if " " not in time_start:
      print "breaking"
      break
    print 'Start: %s  End: %s'%(time_start, time_end)
    print ''

username = 'your_email@gmail.com'
visibility = 'private-lots of numbers here' # private for obvious reasons
projection = 'full'
query = gdata.calendar.service.CalendarEventQuery(username, visibility, projection)
calendar_service = gdata.calendar.service.CalendarService()

DateRangeQuery(calendar_service, start_date, end_date)

# you can also add more calendars at once
username = 'someone_else@gmail.com'
visibility = 'private-numbers12345'
projection = 'full'
query = gdata.calendar.service.CalendarEventQuery(username, visibility, projection)
calendar_service = gdata.calendar.service.CalendarService()

DateRangeQuery(calendar_service, start_date, end_date)

# rinse and repeat
# ...
