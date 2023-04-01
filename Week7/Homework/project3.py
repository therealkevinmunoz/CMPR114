def main():
    sentence = input("Enter a sentence: ")

    new_sentence = sentence_converter(sentence)
    #displays the character that appears most frequently in the string
    print(f"{new_sentence}")

#accepts as input a sentence in which all of the words are run together
def sentence_converter(string): 
    sentence = ''

    firstWord = True
    for ch in string:
        if ch.isupper() and firstWord == True:
            firstWord = False
            sentence += ch
        elif ch.isupper() and firstWord == False:
            new_ch = ' ' + ch.lower()
            sentence += new_ch
        elif ch.islower():
            sentence += ch

    return sentence

#Convert the sentence to a string in which the words are separated by spaces, and only the first word starts with an uppercase letter.

if __name__ == '__main__':
    main()