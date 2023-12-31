def clustered_binary_insertion_sort(arr):
    pop = 0
    for i in range(1, len(arr)):
        cop = i
        key = arr[cop]

        if key >= arr[pop]:
            place = binary_loc_finder(arr, pop+1, cop-1, key)
        else:
            place = binary_loc_finder(arr, 0, pop-1, key)
        
        pop = place
        arr = place_inserter(arr, pop, cop)

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
    # Algo 1: shifting elements in old array
    temp = arr[end]

    for i in range(end, start, -1):
        arr[i] = arr[i-1]
    
    arr[start] = temp
    return arr

    # Algo 2: more efficient but returning new array instead shifting element in old array
    # if end > start:
    #     arr = arr[:start] + [arr[end]] + arr[start:end] + arr[end+1:]
    # else:
    #     arr[start] = arr[end]
    # return arr

# arr = []
# for i in range(5, 0, -1):
#     arr.append(i)

# print("before", arr)
# clustered_binary_insertion_sort(arr)
# print("after", arr)