import random

messages = ['It is certain', 'It is decided so', 'Yes definitely',
            'Reply hazy try again', 'Ask again later',
            'Concentrate and ask again later', 'My reply is no',
            'Outlook good', 'Very doubtful']

print('Ask a yes or no question: ')
input('>')
print(messages[random.randint(0, len(messages) - 1)])