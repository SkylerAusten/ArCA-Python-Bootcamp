from random import *

number1 = random()

a = 0
b = 2
number2 = randint(10, 20)

list = ["A", "B", "C", "D"]
item = choice(list)

print(item)


suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

suite = choice(suites)
card = choice(cards)

print("Your card is:", card, "of", suite)