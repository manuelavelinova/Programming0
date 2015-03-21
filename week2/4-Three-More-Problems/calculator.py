a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

operation = input("Enter operation: ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("There is no such operation")
