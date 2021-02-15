import requests
import huum_config
#


url = 'https://api.huum.eu/action/home/stop'
#myobj = {'targetTemperature' : 40}
x = requests.post(url, auth=(huum_config.usern,huum_config.passw))
print(x.json())

