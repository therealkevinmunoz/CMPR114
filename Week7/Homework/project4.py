def main():
    sentence = input("Enter a sentence to be converted to pig latin: ")
    print(f"Pig Latin: {pig_latin_converter(sentence)}")

def pig_latin_converter(sentence):
    sentence_array = sentence.split(' ')
    new_sentence_array = []
    
    #remove the first letter
    for word in sentence_array:
        first_letter = word[0]
        new_word = ''
        if len(word) > 1:
            new_word = word.replace(word[0], '')
            #place that letter at the end of the word
            new_word += first_letter
        elif len(word) == 1:
            new_word = word

        #append the string “ay” to the word.
        new_word += 'ay'
        new_sentence_array.append(new_word)

    new_sentence = ''
    for word in new_sentence_array:
        new_sentence += word
        new_sentence += " "
    return new_sentence
    
if __name__ == '__main__':
    main()