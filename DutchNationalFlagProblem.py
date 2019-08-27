def sort_012(input_list):
    if len(input_list) == 0:
        return input_list
    # current index
    c = 0
    # head index
    h = 0
    # tail index
    t = len(input_list) - 1
    # The idea is to swap the items when they are in the incorrect spots

    # while head and tail do not pass or equal each other and current has to be less than the tail
    while h < t and c <= t:
        # If it's a 0 then I swap it with the head
        # Then I recheck if this new swapped value needs to be corrected
        if input_list[c] == 0 and c != h:
            input_list[h], input_list[c] = input_list[c], input_list[h]
            h += 1
            continue

        # If it's a 1 then I let it be
        elif input_list[c] == 1:
            c += 1
            continue

        # If it's a 2 then I swap it with the head
        # Then I recheck if this new swapped value is in the correct spot.
        elif input_list[c] == 2:
            input_list[c], input_list[t] = input_list[t], input_list[c]
            t -= 1
            continue
        c += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test cases:
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
