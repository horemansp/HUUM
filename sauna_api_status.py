import requests
import huum_config
#

url = 'https://api.huum.eu/action/home/status'
#enter your username and password from app
usern = 'yourusername@something.bla'
passwo = 'thepassword of your app'
x = requests.get(url, auth=(usern,passw))
print(x.json())

