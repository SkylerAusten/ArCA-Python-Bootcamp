import requests

URL = "http://192.241.154.147/pokemon.html"
page = requests.get(URL)
text = page.text
lines = text.split("\n")

pokemon_file = open("pokemon.txt", "w")

for line in lines:
  if "<td>" in line:
    details = line.replace("</td><td>", "\t")
    details = details.strip("<tr><td>")
    details = details.strip("<td></tr>")

    pokemon_file.write(x + "\n")
  
