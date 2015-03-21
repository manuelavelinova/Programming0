n = input("Enter n: ")
n = int(n)

start = 1

list = []

evens = 0

while start <= n:
    number = input()
    number = int(number)
    start += 1
    list = list + [number]
    if number % 2 == 0:
        evens += 1
print("Count of evens: "+ str(evens))
print("Evens are: ")

for number in list:
    if number % 2 == 0:
          print(number)

    
