while True:
    print('Who are you?')
    name = input('> ').lower()
    if name != 'joe':
        continue
    print('Hello, Joe. What is the password? (it is a fish)')
    password = input('> ').lower()
    if password == 'swordfish':
        break
print('Acces granted!')