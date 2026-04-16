my_pets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name: ')
pet_name = input()

if pet_name not in my_pets:
    print(f'I do not have a pet named {pet_name}')
else:
    print(f'I have a pet named {pet_name}')

