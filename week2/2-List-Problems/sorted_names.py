n = input("Enter n: ")
n = int(n)

start = 1
names = []

while start <= n:
    name = input()
    names += [name]
    start += 1
    
newNames = sorted(names)

for name in newNames:
    print(name)
    
