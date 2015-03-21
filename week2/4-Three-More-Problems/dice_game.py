from random import randint

n = input("Enter n: ")
n = int(n)

first = input("Enter your name: ")
second = input("Enter your name: ")

firstRoll = randint(1,n)
secondRoll = randint(1,n)
print(firstRoll)
print(secondRoll)
if firstRoll > secondRoll:
    print(first + " wins.")
if firstRoll < secondRoll:
    print(second + " wins.")
elif  firstRoll == secondRoll:
    print("There is no winner.")
