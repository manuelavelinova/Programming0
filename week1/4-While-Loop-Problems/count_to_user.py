n = input("Pleaase, enter n: ")
n = int(n)

start = 1
end = n
while start <= end:
    print(start)
    start += 1


start = n
end = 1

while start >= end:
    print(start)
    start -= 1
