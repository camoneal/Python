from random import randint

NUM_EXPERIMENTS = 10000
FLIPS_PER_EXPERIMENT = 100

number_of_streaks = 0

for experiment_number in range(NUM_EXPERIMENTS):
    results = [randint(0,1) for _ in range(FLIPS_PER_EXPERIMENT)]

    streak = 0
    for i in range(len(results)):
        if i == 0:
            streak += 1
        elif results[i] == results[i - 1]:
            streak += 1
        else:
            streak = 1

        if streak == 6:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (100 * number_of_streaks / NUM_EXPERIMENTS))
