# Merge sort is used to sort the elements
def merge_sort(arr):
    if len(arr) > 1:
        # Recursion is used to continuously split the array in half.
        mid = len(arr) // 2
        # Using Auxiliary storage here
        left = arr[:mid]
        right = arr[mid:]
        # Traverse the left side of the array
        merge_sort(left)
        # Traverse the right side of the array
        merge_sort(right)
        # Then we merge the left and right side
        merge(arr, left, right)


def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    # I want the array to be in descending order
    while i < len(left) and j < len(right):
        # We let the array at k be the largest values
        if left[i] > right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # One of the two arrays will be left with elements so we dump
    # which ever one still has items in it.
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def rearrange_digits(input_list):

    if len(input_list) == 0:
        return []

    # We sort the list with merge sort
    merge_sort(input_list)

    first_number = ''
    second_number = ''

    for i in range(0, len(input_list)):
        if i % 2 == 0:
            first_number += str(input_list[i])
        else:
            second_number += str(input_list[i])
    # Convert them to ints and return the two numbers
    ans = [int(first_number), int(second_number)]
    return ans


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test case 1:
test_function([[1, 2, 3, 4, 5], [542, 31]])

# Test case 2:
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test case 3:
test_function([[1, 2, 3], [32, 1]])

# Test case 4:
test_function([[], []])

# Test case 5:
test_function([[9, 9, 9, 9, 9, 9], [999, 999]])