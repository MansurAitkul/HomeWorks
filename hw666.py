import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [64, 34, 25, 12, 22, 11, 90]

start_time = time.time()
bubble_sort(arr.copy())
end_time = time.time()
print( arr)
print( end_time - start_time, "seconds")

start_time = time.time()
selection_sort(arr.copy())
end_time = time.time()
print( arr)
print("Time taken:", end_time - start_time, "seconds")

start_time = time.time()
insertion_sort(arr.copy())
end_time = time.time()
print( arr)
print( end_time - start_time, "seconds")

start_time = time.time()
arr_copy = arr.copy()
arr_copy = quick_sort(arr_copy)
end_time = time.time()
print( arr_copy)
print( end_time - start_time, "seconds")

start_time = time.time()
merge_sort(arr.copy())
end_time = time.time()
print( arr)
print( end_time - start_time, "seconds")
