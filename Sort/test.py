import random
from sorting import selection_sort


def test(sort, list):
    print("-=- MESSED UP -=-")
    print(list)
    print()
    print("-=- SORTED -=- ")
    new_list = sort(list)
    print(new_list)
    print()

# Messed up lists
any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 15, 22, 23, 24, 32, 43, 51, 53, 56, 87, 99, 219]

inversed = [117, 90, 84, 81, 77, 67, 51, 50, 49, 42, 41, 34, 32, 21, 16, 8, 6, 4, 2, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 1, 9, 9, 9, 9, 0, 4, 4 ,4 ,4, 5, 4, 7, 1]



if __name__ == '__main__':
    # SELECTION SORT
    test(selection_sort, any_numbers)
    test(selection_sort, already_sorted)
    test(selection_sort, inversed)
    test(selection_sort, repeated)
