# This is a test of Numpy Graphing and Json using data from internet

#Import statements
import urllib
import json
import urllib.request
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#Sample 1
'''import csv

x = []
y = []

with open('example.csv' , 'r') as file:
    plots = csv.reader(file, delimiter = ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label = 'loaded from file')'''

#Sample 2
'''x,y = np.loadtxt('example.csv',delimiter = ',', unpack=True)
plt.plot(x,y, label = 'loaded from file')'''

#Sample 3 - using URL dataset in JSON format

'''def bytespdate2num(fmt, encoding ='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s =b.decode(encoding)
        return strconverter(s)
    return bytesconverter'''


#Sample 4
x = []
y = []
def graph_data(location):


    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+ location + "?key=F3TTF62K96W72EA7MJS2CNL5V"
#Read data from URL
    response = urllib.request.urlopen(url).read().decode()
#Load JSON data into a library
    weather_data = json.loads(response)

    i = 0
    while i < (len(weather_data['days'][0]['hours'])):
        x.append((weather_data['days'][0]['hours'][i]['datetime']))
        y.append((weather_data['days'][0]['hours'][i]['temp']))
        i += 1
    #print(weather_data['days'][0]['hours'][0]['temp'])

#Sample 5
'''def graph_data(location):


    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+ location + "?key=F3TTF62K96W72EA7MJS2CNL5V"
#Read data from URL
    response = urllib.request.urlopen(url).read().decode()
#Load JSON data into a library
    weather_data = []
    split_source = response.split('\n')



    i = 0
    while i < (len(weather_data['days'][0]['hours'])):
        x.append((weather_data['days'][0]['hours'][i]['datetime']))
        y.append((weather_data['days'][0]['hours'][i]['temp']))
        i += 1'''



graph_data('San%20Diego')
plt.plot(x,y, label = 'loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nJust Kidding')
plt.legend()
plt.show()
