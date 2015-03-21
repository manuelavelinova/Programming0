word = input("Enter word: ")
n = input("Enter n: ")
n = int(n)
start = 1
counter = 0
wordsArray = []


while start <= n:
    words = input()
    if words == word:
        counter += 1
        
    wordsArray = wordsArray + [words]
    start += 1
print(str(word) + " is found: " + str(counter) + " times.")
    
