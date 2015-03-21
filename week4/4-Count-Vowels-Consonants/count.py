def count_vowels_consonants(word):

    vowels  = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    
    result = {"vowels" : 0,
              "consonants" : 0
           }
    for char in word:
        if char in vowels:
            result["vowels"] += 1
        else:
            result["consonants"] += 1

    return result

vowelsAndConsonants = count_vowels_consonants("aaaAcccD")
for char in vowelsAndConsonants:
    value = vowelsAndConsonants[char]
    print(str(char) + " : " + str(value))
    
