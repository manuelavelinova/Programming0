word = input("Enter string : ")
n = input("Enter n : ")
n = int(n)

start = 1
words = []
counter = 0
while start <= n:
    w = input()
    words += [w]
    if word in w:
        counter += 1
    start += 1
print(str(word) + " is found  " + str(counter) + " times.")
    
