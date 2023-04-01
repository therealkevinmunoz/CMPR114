def caeser_cipher(sentence, shiftAmount):
    letters_dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26', ' ': '27'}

    formatted_sentence = sentence.lower()
    sentence_array = []
    
    for ch in formatted_sentence:
        sentence_array.append(int(letters_dict[ch]) - 1)

    new_sentence_array = []

    for value in sentence_array:
        new_value = value + shiftAmount
        
        if(new_value == 27):
            new_sentence_array.append(26)
        elif(new_value > 25):
           new_sentence_array.append(new_value - 26)
        else:
            new_sentence_array.append(new_value)
    
    letters_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    new_sentence = ''

    for value in new_sentence_array:
        new_sentence += letters_array[value]

    return new_sentence
    

print(caeser_cipher("Zebra and monkey", 1))