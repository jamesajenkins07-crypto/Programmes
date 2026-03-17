def countVowels(word):
    numVowels = 0
    word = word.lower()
    
    for letter in word:
        if letter in "aeiou":
            numVowels+=1
    
    return numVowels

print(countVowels("AEIOu"))
