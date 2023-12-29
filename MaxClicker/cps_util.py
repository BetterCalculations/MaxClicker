import random

operator_list = ["+", "-"]


def randomise_cps(array):
    # return randomised cps
    return int(eval(f"{random.randint(array[1], array[0])} {random.choice(operator_list)} {random.randint(1, 2)} "))
