a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

if a < b:
    while a <= b:
        print(a)
        a += 1
else:
    while b <= a:
        print(b)
        b += 1
