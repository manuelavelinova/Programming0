n = input("Enter n  : ")
n = int(n)

start = 1
counter = 0
numbers = []
while start <= n:
    number = input()
    number = int(number)
    if number % 2 == 0:
        numbers += [number]
        counter += 1
        start += 1
    else:
        start += 1
print("Sum of evens is: " + str(counter))
print("Evens are: ")
print(numbers)
