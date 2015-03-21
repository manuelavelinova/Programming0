n = input("Enter n : ")
n = int(n)

divisors = []
start = 1

while start <= n - 1:
    if n % start == 0:
        divisors += [start]

    start += 1

print(divisors)
        
