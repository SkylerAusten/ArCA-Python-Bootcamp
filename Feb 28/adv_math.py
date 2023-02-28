import requests

URL = "http://192.241.154.147/advanced.php"
page = requests.get(URL)
text = page.text
lines = text.split("\n")

for line in lines:
  if " = " in line:
    parts = line.split(" ")
    print(parts)
    num1 = int(parts[0])
    num2 = int(parts[2])
    symbol = parts[1]

    if (symbol == "+"):
      print(num1 + num2)
      
    elif (symbol == "-"):
      print(num1 - num2)

    elif (symbol == "*"):
      print(num1 * num2)

    elif (symbol == "/"):
      print(num1 / num2)

    elif (symbol == "%"):
      print(num1 % num2)

    else:
      print("Oh no!")