def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_loc_finder(arr, 0, i-1, val)
        # arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]

        arr = place_inserter(arr, j, i)

    return arr

def binary_loc_finder(arr, start, end, key):
    mid = start + (end - start) // 2

    if end < start:
        return start;
    
    if end == start:
        if key < arr[mid]:
            return mid
        else:
            return mid+1

    if arr[mid] < key:
            return binary_loc_finder(arr, mid+1, end, key)
    else:
        return binary_loc_finder(arr, start, mid-1, key)
 
def place_inserter(arr, start, end):
    temp = arr[end]

    for i in range(end, start, -1):
        arr[i] = arr[i-1]
    
    arr[start] = temp
    return arr
 
print("Sorted array:")
print(binary_insertion_sort([5,4,1,3,2]))