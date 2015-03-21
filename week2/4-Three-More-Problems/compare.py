a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if a > b:
    print("a > b")
elif a < b:
    print("b > a")
else:
    print(str(a) + " is equal to " + str(b))
