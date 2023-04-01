def main():
    sentence = input("Enter a sentence: ")
    #display the number of vowels and consonants it contains
    print(f"Vowel Count: {vowel_count(sentence)}\nConsonant Count: {consonant_count(sentence)}")

#a function that accepts a string as an argument and returns the #number of vowels that the string contains. 
def vowel_count(sentence):
    vowel_count = 0
    lowercase_sentence = sentence.lower()
    for ch in lowercase_sentence:
        if ch == 'a':
            vowel_count += 1
        elif ch == 'e':
            vowel_count += 1
        elif ch == 'i':
            vowel_count += 1
        elif ch == 'o':
            vowel_count += 1
        elif ch == 'u':
            vowel_count += 1
    return vowel_count

#a function that accepts a string as an argument and returns the number of consonants that the string contains. 
def consonant_count(sentence):
    consonant_count = 0
    isVowel = False
    lowercase_sentence = sentence.lower()
    for ch in lowercase_sentence:
        if ch.isalpha():
            if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                isVowel = True
            else:
                consonant_count += 1

    return consonant_count

if __name__ == '__main__':
    main()