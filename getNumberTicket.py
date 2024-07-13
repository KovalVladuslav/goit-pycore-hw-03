import random


def get_numbers_ticket(min, max, quantity):
    try:
        numberMin = int(min)
        numberMax = int(max)

        if numberMin < 1 or numberMax > 1000:
            return []

        all_mumbers = list(range(numberMin, numberMax + 1))
        random_list = random.sample(all_mumbers, quantity)

        return sorted(random_list)
    except ValueError:
        print("You should enter numbers")


print(get_numbers_ticket(1, "hffyg", 3))