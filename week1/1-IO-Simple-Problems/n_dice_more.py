from random import randint
n = input("Enter sides:")
n = int(n)

print("First roll:")
result1 = randint(1,n)
print(result1)

print("Second roll:")
result2 = randint(1,n)
print(result2)

print("Third roll:")
result3 = randint(1,n)
print(result3)

print("Sum is:")
result = result1 + result2 + result3
print(result)
