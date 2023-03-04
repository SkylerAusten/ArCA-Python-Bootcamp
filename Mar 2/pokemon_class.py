import requests

URL = "http://192.241.154.147/pokemon.html"
page = requests.get(URL)
text = page.text
lines = text.split("\n")

pokemon_file = open("pokemon.txt", "w")

pokedex = []

for line in lines:
  if "<td>" in line:
    details = line.replace("</td><td>", "\t")
    details = details.strip("<tr><td>")
    details = details.strip("<td></tr>")
    details = details + "\n"

    pokemon = details.split("\t")

    # ['649', 'Genesect', '71', '120', '95', '120', '95', '99', '600', 'Bug', 'Steel\n']
    temp = {}
    temp["id"] = pokemon[0]
    temp["name"] = pokemon[1]
    temp["hp"] = pokemon[2]
    temp["atk"] = pokemon[3]
    temp["def"] = pokemon[4]
    temp["spa"] = pokemon[5]
    temp["spd"] = pokemon[6]
    temp["spe"] = pokemon[7]
    temp["total"] = pokemon[8]
    temp["type1"] = pokemon[9]
    temp["type2"] = pokemon[10]

    pokedex.append(temp)

pokedex.pop(0)

for pokemon in pokedex:
  print(pokemon["hp"])
  break