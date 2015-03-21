text = input("Enter string: ")

counter = 0
vowels = "aeiouyAEIOUY"

for letter in text:
    if letter in vowels:
        counter += 1
print(counter)
