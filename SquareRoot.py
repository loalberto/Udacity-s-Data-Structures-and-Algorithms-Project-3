def square_root(num):
    if num is None or num < 0:
        return None
    start = 0
    end = num
    mid = (start + end) // 2
    # I used a binary search implementation to help me find the floor
    # value or exact value of the square root.
    # Binary Search has a time complexity of O(logn)
    while start <= mid <= end:
        if mid ** 2 == num:
            return mid
        if mid ** 2 > num:
            end = mid - 1
            mid = (start + mid) // 2
            continue
        if mid * mid < num:
            if (mid + 1) ** 2 > num:
                return mid
            start = mid + 1
            mid = (start + end) // 2


# Test 1
print("Pass" if square_root(100) == 10 else "Fail")

# Test 2
print("Pass" if square_root(21343235763245465) == 146093243 else "Fail")

# Test 3
print("Pass" if square_root(None) is None else "Fail")

# Test 4:
print("Pass" if square_root(-12) is None else "Fail")