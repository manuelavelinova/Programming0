n = input("Enter n : ")
n = int(n)

start = 1
numbers = []
while start <= n:
    number = input()
    number = int(number)
    numbers += [number]
    start += 1
    
min = numbers[0]

for number in numbers:
    if number < min:
        min = number
print(min)
