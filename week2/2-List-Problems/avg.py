n = input("Enter n: ")
n = int(n)

start = 1
counter = 0
sum = 0

while start <= n:
    number = input()
    number = int(number)
    start += 1
    counter += 1
    sum += number
avg = sum / counter
print("Avg is : " + str(avg))    
    
