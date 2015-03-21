n = input("Enter n : ")
n = int(n)

start  = 1
sum = 0 
while start <= n:
    number = input()
    number = int(number)
    sum += number
    start += 1
print("Sum is : "  + str(sum))
