def main():
    user_string = input("Enter a string: ")

    print("This is what I found about the string")

    if user_string.isalnum():
        print('This string is alphanumeric')
    if user_string.isdigit():
        print('This string is a number')
    if user_string.isalpha():
        print('This string is only alphabetic characters')
    if user_string.isspace():
        print('This string only contains whitespace characters')
    if user_string.islower():
        print('The characters in this string are all lowercase')
    if user_string.isupper():
        print('The characters in this string are all uppercase')

if __name__ == '__main__':
    main()

