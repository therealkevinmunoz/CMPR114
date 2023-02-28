FIRST_NAME = ['Kevin'];
LAST_NAME = ['Munoz'];
full_name = '';

for name in FIRST_NAME:
    full_name += name
    full_name += ' ';

for name in LAST_NAME:
    full_name += name

print(f'Your full name is {full_name}')