from calendar import month
from xml.dom import minidom
import re
from datetime import date

class stepTracker:
    
    def __init__():
        steps = 0
        avgSteps = 0

    def getAvgSteps(filename):
        pattern = '(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s{1}(?P<time>\d{2}:\d{2}\:\d{2})\s{1}(?P<gmt_offset>.\d{4})' #2015-11-03 22:43:31 +0800
        xmldoc = minidom.parse(filename)
        recordlist = xmldoc.getElementsByTagName('Record')
        avgSteps = 0
        instanceList = []
        for s in recordlist:
            if s.attributes['type'].value == 'HKQuantityTypeIdentifierStepCount':
                m = re.match(pattern, s.attributes['startDate'].value)
                if m:
                    try:
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

        return int(avgSteps / int(dayCounter.days))