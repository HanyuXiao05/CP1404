import random

PICKS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

picks_number = int(input('How many quick picks? '))

for i in range(picks_number):
    pick = []
    for j in range(PICKS_PER_LINE):
        random_number = random.randint(MIN_NUMBER,MAX_NUMBER)
        while random_number in pick:
            random_number = random.randint(MIN_NUMBER,MAX_NUMBER)
        pick.append(random_number)
    pick.sort()
    pick = [f'{str(k):>2}' for k in pick]
    pick = ' '.join(pick)
    print(pick)