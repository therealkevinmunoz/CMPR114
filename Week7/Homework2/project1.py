import random

def blackjack():
    user_score = 0
    comp_score = 0

    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,  '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10, 'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,  '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10, 'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,  '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,  '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10}
    
    #deal an initial set of card to user and computer
    for count in range(2):
        card = random.choice(list(deck))
        print(card)
        user_score += deck[card]
        
    print(f'Your score: {user_score}')

    for count in range(2):
        card = random.choice(list(deck))
        print(card)
        comp_score += deck[card]
        
    print(f'Computer score: {comp_score}')

    continue_playing_flag = continue_playing()

    while continue_playing_flag == 'y':
        card = random.choice(list(deck))
        print(card)
        user_score += deck[card]
        print(f'Your score: {user_score}')

        card = random.choice(list(deck))
        print(card)
        comp_score += deck[card]
        print(f'Computer score: {comp_score}')

        if(user_score == 21 or comp_score > 21):
            print("You win!")
            break
        elif(comp_score == 21 or user_score > 21):
            print('You lose!')
            break
        elif (comp_score > 21 and user_score > 21):
            print('You both lose!')
            break
        else:
            continue_playing_flag = continue_playing()

    if continue_playing_flag != 'y':
        if comp_score > user_score:
            print('You lose!')
        elif user_score > comp_score:
            print('You win!')
        elif user_score == comp_score:
            print('It\'s a tie!')


def continue_playing():
    continue_flag = input("Would you like to hit? (y = yes, any other key = no) ")
    #while continue_flag != "y" or continue_flag != "n":
        #print('Invalid input')
        #continue_flag = input("Would you like to hit? (y = yes, n = no) ")
    return continue_flag

blackjack()