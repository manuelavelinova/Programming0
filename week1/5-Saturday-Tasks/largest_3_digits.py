n = input("Enter number that has 3 integers: ")
n = int(n)

a = n % 10
b = (n // 10) % 10
c = n // 100

if a >= b and a >= c and b >= c:
    print(str(a) + str(b) + str(c))
    
elif a >= b and a >= c and b <= c:
    print(str(a) + str(c) + str(b))

elif b >= a and b >= c and a >= c:
    print(str(b) + str(a) + str(c))
    
elif b >= a and b >= c and a <= c:
    print(str(b) + str(c) + str(a))
    
elif c >= a and c >= b and a >= b:
    print(str(c) + str(a) + str(b))
    
elif c >= a and c >= b and a <= b:
    print(str(c) + str(b) + str(a))
