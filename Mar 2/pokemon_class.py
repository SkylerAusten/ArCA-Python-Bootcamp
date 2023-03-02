import requests

URL = "http://192.241.154.147/pokemon.html"
page = requests.get(URL)
text = page.text
lines = text.split("\n")

pokemon_file = open("pokemon.txt", "w")

for line in lines:
  if "<td>" in line:
    x = line.replace("</td><td>", "  ")
    x = x.strip("<tr><td>")
    x = x.strip("<td></tr>")
    # list = x.split("  ")
    # print(list)

    pokemon_file.write(x + "\n")
  
