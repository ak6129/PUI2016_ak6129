from __future__ import print_function
import pylab as pl
import json
import urllib as urllib
import sys
import csv


key = sys.argv[1]
bus_id = sys.argv[2]
csv_out = sys.argv[3]

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=3757e20b-a934-4ff6-a857-60a74ea04a2b&VehicleMonitoringDetailLevel=calls&LineRef=B52"
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + bus_id
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

position = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

fout = csv.writer(open(sys.argv[3], 'wb'))

fout.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])


for i in position:
    #Latitude,Longitude,Stop Name,Stop Status
    latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    stopname = i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    stopstatus = i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']  
    fout.writerow([latitude,longitude,stopname,stopstatus])
