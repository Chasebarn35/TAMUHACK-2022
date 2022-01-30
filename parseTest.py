from calendar import month
from xml.dom import minidom
import re
#import csv
from datetime import date



pattern = '(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s{1}(?P<time>\d{2}:\d{2}\:\d{2})\s{1}(?P<gmt_offset>.\d{4})' #2015-11-03 22:43:31 +0800
xmldoc = minidom.parse("export.xml")
recordlist = xmldoc.getElementsByTagName('Record')
avgSteps = 0
instanceList = []
for s in recordlist:
    if s.attributes['type'].value == 'HKQuantityTypeIdentifierStepCount':
        m = re.match(pattern, s.attributes['startDate'].value)
        if m:
            try:
                print ('%s,%s,%s,%s,%d' % (m.group('year'), m.group('month'), m.group('day'), m.group('time'),   float(s.attributes['value'].value)))
                instanceList.append([m.group('year'), m.group('month'), m.group('day'), float(s.attributes['value'].value)])


            except:
                print ('in except block, TODO!')



if(len(instanceList) > 3000):
    instanceList = instanceList[len(instanceList)-3000 : len(instanceList)-1]

startDate = date(int(instanceList[0][0]), int(instanceList[0][1]), int(instanceList[0][2]))
endDate = date(int(instanceList[len(instanceList)-1][0]), int(instanceList[len(instanceList)-1][1]), int(instanceList[len(instanceList)-1][2]))

dayCounter = endDate - startDate

for i in instanceList:
    avgSteps += int(i[3])

            
print(instanceList[0], instanceList[len(instanceList)-1])
print(int(dayCounter.days))
print(int(avgSteps / int(dayCounter.days)))