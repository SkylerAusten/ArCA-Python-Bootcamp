import requests

URL = "http://192.241.154.147"
page = requests.get(URL)
text = page.text