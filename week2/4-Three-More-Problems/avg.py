n = input("Enter n : ")
n = int(n)

start = 1
sum = 0
count = 0 
while start <= n:
    number = input()
    number = int(number)
    sum += number
    count += 1
    start += 1
avg = sum / count
print(avg)
    
