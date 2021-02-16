import requests
import huum_config
#


url = 'https://api.huum.eu/action/home/stop'
#enter your username and password from app
x = requests.post(url, auth=(usern,passw))
print(x.json())

