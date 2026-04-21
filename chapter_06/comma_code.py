

spam = ['apples', 'bananas', 'tofu', 'cats']

def formated_string(stuff):
    # Pista: Si la lista está vacía, terminamos temprano
    if len(stuff) == 0:
        return "The list is empty."

    final_string = ''
    for i in range(len(stuff)):
        if i == (len(stuff) -1):
            final_string += 'and ' + stuff[i]
        else:
            final_string += stuff[i] + ', '

    return final_string

formated_spam = formated_string(spam)
print(formated_spam)