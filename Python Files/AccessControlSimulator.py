# A simple access control simulator

username = input('Enter Username: ')

if username.upper() == 'USERNAME':
    password = input('Enter Password: ')
    if password == 'SUNWAY':
        print('ACCESS GRANTED!.')
    else:
        print('ACCESS DENIED!')
else:
    print('ACCESS DENIED!')
