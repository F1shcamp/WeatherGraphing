# This is a test of Numpy Graphing
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

#Sample 3
def graph_data(location):
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+ location + "?key=F3TTF62K96W72EA7MJS2CNL5V"
    response = urllib.request.urlopen(url).read().decode()
    weather_data = json.loads(response)
    i = 0
    while i < (len(weather_data['days'])):
        print(str(weather_data['days'][i]['dew']) + '\n')
        i += 1




graph_data('San%20Diego')

''' plt.plot(x,y, label = 'loaded from file')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interesting Graph\nJust Kidding')
    plt.legend()
    plt.show()

graph_data(urllib.parse.quote('London, UK', safe=''))
'''
