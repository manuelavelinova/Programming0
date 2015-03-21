n = input("Enter n: ")
n = int(n)

start = 1
divisors = []
while start < n:
    if n % start == 0:
        divisors += [start]
        start += 1
    else:
        start += 1
print("Divisors of  " + str(n) + " are " + str(divisors)) 
    
        
