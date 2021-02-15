import requests
import huum_config
#

url = 'https://api.huum.eu/action/home/status'
x = requests.get(url, auth=(huum_config.usern,huum_config.passw))
print(x.json())

