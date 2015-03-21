def count_words(words):
    result = {}
    
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

wordss = count_words(["words", "are", "meaningful", "words", "words", "are"])

for char in wordss:
    value = wordss[char]
    print(str(char) + " : " + str(value))
