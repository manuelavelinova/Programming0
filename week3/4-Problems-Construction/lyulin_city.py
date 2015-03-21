n = input("Enter n: ")
n = int(n)

start = 0
end = n - 1

buildings = []
while start <= end:
    building = input("Enter the heigh of the building : ")
    buildings += [building]
    start += 1
    
tallest = buildings[0]
count = 1


for building in buildings:
    if building > tallest:
        tallest = building
        count += 1
print(count)

