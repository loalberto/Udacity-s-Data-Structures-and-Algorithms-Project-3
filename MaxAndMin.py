import random
# This will find the max and min values in a single traversal


def get_min_max(ints):
    if len(ints) == 0:
        return ()
    mi = ints[0]
    ma = ints[0]
    # I look for both min and max at the same time
    for i in range(0, len(ints)):
        if ints[i] < mi:
            mi = ints[i]
        if ints[i] > ma:
            ma = ints[i]
    return mi, ma


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = []
random.shuffle(l)
print("Pass" if (() == get_min_max(l)) else "Fail")

l = [1]
print("Pass" if (1, 1) == get_min_max(l) else "Fail")