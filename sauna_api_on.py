
import requests

url = 'https://api.huum.eu/action/home/start'
myobj = {'targetTemperature' : 40}
#enter your username and password from app
usern = 'yourusername@something.bla'
passw = 'thepassword of your app'
x = requests.post(url, data = myobj, auth=(usern,passw))
print(x.json())

