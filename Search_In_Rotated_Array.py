# I use a binary search approach to find the pivot where the list
# is rotated to preserve the worst case of logn.

def find_pivot(arr):
    if arr[0] > arr[1]:
        return 0
    if arr[len(arr) - 1] < arr[len(arr) - 2]:
        return 0
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    while start <= mid <= end:
        # If the middle value is in between a bigger and
        # smaller value then This is our pivot index
        if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
            return mid
        # If the value is bigger than both its previous and next values
        # Then we are right next to the pivot.
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            start = mid + 1
            mid = (start + end) // 2
            continue
        # If it is a value in a sorted list then we need to decide where to traverse
        if arr[mid - 1] < arr[mid] < arr[mid + 1]:
            if end == len(arr):
                end -= 1
            # If the mid value is less than the end value then our value
            # has to be on the left side, since our pivot was not our current middle
            # value and anything before it is smaller than our middle value.
            if arr[mid] < arr[end]:
                end = mid - 1
                mid = (start + end) // 2
            # Else if the start value is bigger than the middle value then the pivot
            # point is on the right since all our smaller values will be there.
            else:
                start = mid + 1
                mid = (start + end) // 2


def rotated_array_search(arr, num):
    if arr is None or len(arr) == 0 or num is None:
        return -1
    # If the lenght of the array is 1 and arr[0] == num then I return index 0 .
    if len(arr) == 1:
        if arr[0] == num:
            return 0
        return -1
    pivot = find_pivot(arr)
    # The pivot is at the beginning so I search from start to end
    if pivot == 0:
        return binary_search(arr, pivot, len(arr) - 1, num)
    # If the pivot is at the end then I search from the start to the end - 1
    elif pivot == len(arr) - 1:
        return binary_search(arr, 0, pivot - 1, num)
    else:
        # If the pivot is in between the start and end then I check
        # whether the number is greater than the last digit.
        if num > arr[len(arr) - 1]:
            # If it is then I search from the start to the pivot - 1
            # because since the pivot is the smallest element and our number 
            # exceeds the last element then the number could to be on the list to the left of the pivot
            return binary_search(arr, 0, pivot - 1, num)
        else:
            # But if it's smaller then I search from the pivot to the end. 
            # Since it might be to the right of the pivot
            return binary_search(arr, pivot, len(arr) - 1, num)

# My implementation of binary search
def binary_search(arr, low, high, val):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            return binary_search(arr, low, mid - 1, val)
        if arr[mid] < val:
            return binary_search(arr, mid + 1, high, val)
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])

# Trying non-existent values
test_function([[6, 7, 8, 0, 1, 2, 3, 4], 10])
test_function([[3, 4, 5, 6, 1, 2], 8])

# Trying it with negative numbers
test_function([[5, 6, -2, -1, 2, 3, 4], -3])

# Trying empty values
test_function([[], 2])
