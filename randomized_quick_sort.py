import random

def randomized_quick_sort(arr):
    randomized_quick_sort_rec(arr, 0, len(arr)-1)

def randomized_quick_sort_rec(arr, left, right):
    if left < right:
        final_pivot_pos = randomized_partition(arr, left, right)
        randomized_quick_sort_rec(arr, left, final_pivot_pos-1)
        randomized_quick_sort_rec(arr, final_pivot_pos+1, right)

def randomized_partition(arr, left, right):
    random_number = random.randint(left, right)
    swap(arr, random_number, right)
    pivot = arr[right]

    last_filled = left-1

    for i in range(left, right):
        if (arr[i] <= pivot):
            last_filled += 1
            swap(arr, last_filled, i)

    last_filled += 1
    swap(arr, last_filled, right)
    return last_filled

def swap(arr, index1, index2):
    arr[index1], arr[index2]  = arr[index2], arr[index1]


# arr = [5,4,1,3,2,6, 0]
# print("before", arr)
# randomized_quick_sort(arr)
# print("after", arr)