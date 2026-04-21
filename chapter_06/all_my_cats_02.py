cat_names = []
while True:
    print(f'Enter the name of the cat: {len(cat_names)} or enter "quit" to exit: ')
    cat_name = input()
    if cat_name == 'quit':
        break
    cat_names.append(cat_name)

print('The cat names are:')
for cat_name in cat_names:
    print(cat_name)