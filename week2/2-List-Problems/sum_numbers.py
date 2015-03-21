n = input("Enter n : ")
n = int(n)

start = 1
maxSum = 0

while start <= n:
    number = input()
    number = int(number)
    maxSum += number
    start += 1
print("The sum is: " + str(maxSum))
    
