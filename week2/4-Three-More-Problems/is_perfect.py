n = input("Enter n : ")
n = int(n)

start = 1
sum = 0

while start <= n - 1:
    if n % start == 0:
        sum += start
    start += 1

if sum == n:
    print("Its perfect")
else:
    print("Its not perfect")
