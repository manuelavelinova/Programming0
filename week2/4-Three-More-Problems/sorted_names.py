n = input("Enter n : ")
n = int(n)

start  = 1
names = []

while start <= n:
    name = input()
    names += [name]
    start += 1
sortednames = sorted(names)

for name in sortednames:
    print(name)
    
