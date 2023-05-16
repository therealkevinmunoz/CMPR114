#Importing mbti.csv file into tuple
import csv
import os
import openai

#User object sets and gets mbti
class User:
  def __init__(self, mbti='unknown'):
    self.__mbti = mbti
    self.__mbti_tuple, self.__mbti_description_tuple = self.database()
  def set_mbti(self,mbti):
    self.__mbti = mbti
  def get_mbti(self):
    return self.__mbti
  def database(self):
    with open('./GroupProject/MBTI.csv','r',encoding='utf-8') as file:
      reader = csv.reader(file)
      mbti = []
      mbti_description = []
      for row in reader:
        mbti.append(row[0])
        mbti_description.append(row[1])
    mbti_tuple = tuple(mbti)
    mbti_description_tuple = tuple(mbti_description)
    return mbti_tuple, mbti_description_tuple
  def get_user_input(self):
    print('There are 4 aspects of the personality: \nMind (Introverted, Extrovered), Energy (Observant, Intuitive), Nature (Thinking, Feeling), Tactics (Judging, Prospecting)')
    should_take_input = True
    while should_take_input:
      try:
        mbti = input('\nWhich is your MBTI? ').upper()
        index = self.__mbti_tuple.index(mbti)
        print(f'{self.__mbti_description_tuple[index]}')
        self.set_mbti(mbti)
        should_take_input = False
      except ValueError as e:
        print('Please enter the correct MBTI')

#Class object is used to hold all methods related to application
class App:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        #Dictionary is used to store items from conversation
        self.__chat_dictionary = {}

    def start_app(self):
        print('----Welcome to the MBTI Personality Chatbot----\n')
        print('Here is an introduction to MBTIs...')
        main_user = User()
        main_user.database() 
        main_user.get_user_input()
        self.handle_interaction(main_user)
        additional_questions_running = True
        while(additional_questions_running):
            chat_array = self.ask_additional(main_user)
            self.add_conversation(chat_array[0], chat_array[1])
            app_continue = input('\nWould you like to ask something else? (y = yes, anything else = no) ')
            if app_continue != 'y':
                additional_questions_running = False
                self.write_external_file(self.__chat_dictionary)

    def ask_additional(self, user):
        user_input = input(f"\nAsk more about {user.get_mbti()}: ")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ])
        chat_response = completion.choices[0].message.content
        print(f'\nChatGPT: {chat_response}')
        #Array list is used to return user response and chat response
        return [user_input, chat_response]

    
    def add_conversation(self, user_input, chat_response):
        self.__chat_dictionary[user_input] = chat_response

    def write_external_file(self, list):
        external_file = open('GroupProject/chat_transcript.txt', 'w')
        #Loop is used to parse through the items in the conversation dictionary
        for item in list:
            external_file.write(f'You: {item}\nChatGPT: {list[item]}\n')
        external_file.close()
        print('\nYour file chat_transcript.txt has been created')

    def show_menu(self):
        print("\nWhich area of life do you want to know how your MBTI interacts with?")
        print("1. Love")
        print("2. Career")
        print("3. Friendship")
        area_choice = input("\nEnter your choice(1, 2, or 3): ")
        area_choice_values = ['N/A', 'Love', 'Career', 'Friendship']
        while area_choice not in ["1","2", "3" ]:
            print("Invalid Input. Please choose either 1, 2, or 3")
            area_choice = input("Enter your choice (1, 2, or 3): ") 
        return area_choice_values[int(area_choice)]

    def handle_interaction(self, user):
        area_choice = self.show_menu()
        user_input = f"Tell me about {area_choice} for the MBTI personality: {user.get_mbti()}."
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": user_input}
            ])
        chat_response = completion.choices[0].message.content
        print(f'\nChatGPT: {chat_response}')
        self.add_conversation(user_input, chat_response)

myApp = App()
myApp.start_app()