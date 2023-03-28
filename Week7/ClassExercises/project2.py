#import login

def get_login_name(first, last, idnumber):
    if len(first) >= 3:
        set1 = first[0:3]
    else:
        set1 = first

    if len(last) >= 3:
        set2 = last[0:3]
    else:
        set2 = last
  
    if len(idnumber) >= 3:
        set3 = idnumber[-3 :]
    else:
        set3 = idnumber

    login_name = set1 + set2 + set3
    return login_name
    
print(get_login_name("Kevin", "Munoz", "12342"))

def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digits = False

    if len(password) >= 7:
        correct_length = True
    
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digits = True
    
    if correct_length and has_uppercase and has_lowercase and has_digits:
        is_valid = True
    else:
        is_valid = False

    return is_valid


def main():
    password = input("Enter you password: ")

    while not valid_password(password):
        print("This password is not valid")
        password = input("Enter you password: ")

    print("This is a valid password.")

if __name__ == '__main__':
    main()
