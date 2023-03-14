import random

def main():
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()

    CHOICES = ("", "Rock", "Paper", "Scissors")

    if((user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1)):
        print(f'You lose. You chose {CHOICES[user_choice]}, computer chose {CHOICES[comp_choice]}.')
    elif((user_choice == 2 and comp_choice == 1) or (user_choice == 3 and comp_choice == 2) or (user_choice == 1 and comp_choice == 3)):
        print(f'You win! You chose {CHOICES[user_choice]}, computer chose {CHOICES[comp_choice]}.')
    elif(user_choice == comp_choice):
        print(f'It\'s a tie! You chose {CHOICES[user_choice]}, computer chose {CHOICES[comp_choice]}. ')

    

def get_user_choice():
    #valid_selection = False
   #while valid_selection == False:

        USER_PICK = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
        
        #if(USER_PICK != 1 or USER_PICK != 2 or USER_PICK != 3):
            #print("Invalid selection")
       # else:
           # valid_selection = True
        return USER_PICK

def get_computer_choice():
    COMP_PICK = random.randint(1,3)
    return COMP_PICK

main()