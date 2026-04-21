

def collatz(number):
    if number % 2 == 0:
        result = number // 2

    else:
        result = 3 * number + 1

    print(result, end= ' ')
    return result
try:
    user_input = int(input('Enter a number: '))
    while user_input != 1:
        user_input = collatz(user_input)
except ValueError:
    print('Error: Debes ingresar un número entero.')