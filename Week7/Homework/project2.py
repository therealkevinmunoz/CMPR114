def main():
    sentence = input("Enter a sentence to search the most frequent character: ")
    frequent_letter = letter_frequency(sentence)

    #displays the character that appears most frequently in the string
    print(f"The character '{frequent_letter}' appears the most in your sentence")

#user enter a string
def letter_frequency(string):
    highest_char = ''
    highest_char_count = 0
    for ch in string:
        if ch.isalnum():
            if string.count(ch) > highest_char_count:
                highest_char = ch
                highest_char_count = string.count(ch)
    
    return highest_char

if __name__ == '__main__':
    main()
