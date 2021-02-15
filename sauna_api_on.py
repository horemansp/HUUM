
import requests
import huum_config

#


url = 'https://api.huum.eu/action/home/start'
myobj = {'targetTemperature' : 40}
x = requests.post(url, data = myobj, auth=(huum_config.usern,huum_config.passw))
print(x.json())

