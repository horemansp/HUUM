import requests

url = 'https://api.huum.eu/action/home/status'
#enter your username and password from app
usern = 'yourusername@something.bla'
passw = 'thepassword of your app'
x = requests.get(url, auth=(usern,passw))
print(x.json())

