n = input("Enter n: ")
n = int(n)

start = 1
numbers = []

while start <= n:
    number = input()
    number = int(number)
    numbers += [number]
    start += 1

maxNumber = numbers[0]

for number in numbers:
    if number > maxNumber:
        maxNumber = number
print("The max is : " + str(maxNumber))
