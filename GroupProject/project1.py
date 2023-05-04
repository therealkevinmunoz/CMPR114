import os
import openai

#Class object is used to hold all methods related to application
class App:
    def __init__(self):
        openai.api_key = "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"
        #Dictionary is used to store items from conversation
        self.__chat_dictionary = {}

    def start_app(self):
        app_running = True
        while(app_running):
            chat_array = self.ask_additional()
            self.add_conversation(chat_array[0], chat_array[1])
            app_continue = input('\nWould you like to ask something else? (y = yes, anything else = no) ')
            if app_continue != 'y':
                app_running = False
                self.write_external_file(self.__chat_dictionary)

    def ask_additional(self):
        user_input = input("Your question: ")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ])
        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
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
        print('Your file chat_transcript.txt has been created')

myApp = App()
myApp.start_app()
