n = input("Enter n : ")
n = int(n)

factorial = 1

if n == 0:
    print(factorial)
    
while n != 1:
    factorial *= n
    n = n - 1

print(factorial)
