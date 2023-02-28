import requests

URL = "http://192.241.154.147"
page = requests.get(URL)
text = page.text
lines = text.split("\n")

for line in lines:
  if " = " in line:
    parts = line.split(" ")
    num1 = int(parts[0])
    num2 = int(parts[2])
    print(parts)
    print(num1 + num2)
