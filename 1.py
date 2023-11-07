apikey="2607e6b4fc75c824f58958cb82a09542"
url="https://api.openweathermap.org/data/2.5/weather"
params={'q':"delhi",'appid':apikey,'units':"metric"}
import requests
data=requests.get(url,params=params)
data.json()
