import random

number_of_streak = 0

for experiment_number in range(1, 10000):
    coin_results = []
    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 1:
            coin_results.append('H')
        else:
            coin_results.append('T')

    for i in range(len(coin_results) -6):
        if (coin_results[i : i +6] == ['H'] * 6 or
                coin_results[i : i +6] == ['T'] * 6):
            number_of_streak += 1
            break

print(f'Chance of streak: {number_of_streak / 100}%')