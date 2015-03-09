start = input("Enter a: ")
end = input("Enter b: ")

start = int(start)
end = int(end)

while start <= end:
    if start % 2 == 0:
        print(str(start) + " is even ")
        start += 1
    else:
        print(str(start) + " is odd ")
        start +=1
