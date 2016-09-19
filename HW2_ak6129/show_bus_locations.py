from __future__ import print_function
import pylab as pl
import json
import urllib2 as urllib
import sys

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=3757e20b-a934-4ff6-a857-60a74ea04a2b&VehicleMonitoringDetailLevel=calls&LineRef=B52"
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2] 

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


(type(data))

data.keys()

data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']

position = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

type(position)

len(position)

busline = 'Bus line:' + sys.argv[2]
numberofbuses = len(position) 
print (busline)
print ('Number of Active Buses :' , numberofbuses)

ii = 0
for i in position:
    
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus', ii, 'is at', latitude, 'and', longitude)
    ii = ii + 1
