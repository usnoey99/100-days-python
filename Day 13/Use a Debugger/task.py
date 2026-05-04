import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])



# FIXED VERSION
import random


def mutate(a_list):
    b_list = []

    for item in a_list:
        new_item = item * 2  # double the item
        new_item += random.randint(1, 3)  # add random 1-3
        new_item += item  # add original item

        b_list.append(new_item)  # append inside the loop

    print(b_list)


mutate([1, 2, 3, 5, 8, 13])