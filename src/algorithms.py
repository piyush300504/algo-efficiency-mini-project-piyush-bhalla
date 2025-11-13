"""
Basic implementations used in the assignment.
Includes: Fibonacci, sorting algorithms, and binary search.
"""

# ---------------- Fibonacci ----------------

def fib_recursive(n):
    # naive recursion: F(n) = F(n-1) + F(n-2)
    # works but gets slow when n is big (like 30+)
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dp(n):
    # bottom-up DP with two vars
    # start from 0 and 1, go till n
    if n < 0:
        raise ValueError("n must be non-negative")
    a = 0  # F(0)
    b = 1  # F(1)
    if n == 0:
        return a
    if n == 1:
        return b
    # update a and b n-1 times
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# ---------------- Sorting ------------------

def merge_sort(arr):
    # returns a new sorted list
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge two sorted lists
    i = 0  # pointer for left
    j = 0  # pointer for right
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def quick_sort(arr):
    # simple recursive quick sort that returns a new list
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[0]  # pick the first element as pivot
    left = []   # values <= pivot
    right = []  # values > pivot
    for x in arr[1:]:  # put every element (except pivot) on one side
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)


def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False  # if nothing swaps in a pass, we stop early
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_index = i  # assume current i is smallest
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


# ---------------- Searching ----------------

def binary_search(arr, target):
    # arr must be sorted, returns index or -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
