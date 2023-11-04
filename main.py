import time
import timeit
import matplotlib.pyplot as plt
import tracemalloc
from clustered_binary_insertion_sort import clustered_binary_insertion_sort
from randomized_quick_sort import randomized_quick_sort

runtime_data = [[[], [], []], [[], [], []]]
memory_data = [[[], [], []], [[], [], []]]

def read_data_file(filename):
    f = open(f"data/{filename}", "r")
    out = f.read()

    arr = out.split(",")
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    f.close()

    return arr

def evaluate_time_and_space(func, filename):
    tracemalloc.start()
    arr = read_data_file(filename)
    
    start = timeit.default_timer()
    # print("before", arr)
    func(arr)
    # print("after", arr)
    malloc = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = timeit.default_timer()
    runtime = (end-start) * 1000
    runtime = float("%.5f" % runtime)
    
    
    print(f"\t\t{func.__name__}")
    print(f"\t\t\tRuntime: {runtime} ms")
    print(f"\t\t\tMemory Allocation: {malloc}")

    return runtime, malloc

def evaluate_with_filename(func1, func2, filename, no):
    runtime1, memory1 = evaluate_time_and_space(func1, filename)
    runtime2, memory2 = evaluate_time_and_space(func2, filename)

    runtime_data[0][no].append(runtime1) # for clustered binary insertion sort
    runtime_data[1][no].append(runtime2) # for randomized quick sort

    memory_data[0][no].append(memory1) # for clustered binary insertion sort
    memory_data[1][no].append(memory2) # for randomized quick sort

def evaluate_all(func1, func2):
    mult = 1
    for i in range(1, 4):
        print(f"SIZE {200*mult}")
        print(f"\tSorted:")
        evaluate_with_filename(func1, func2, f"sorted{i}.txt", i-1)

        print(f"\tRandom:")
        evaluate_with_filename(func1, func2, f"random{i}.txt", i-1)

        print(f"\tReverse:")
        evaluate_with_filename(func1, func2, f"reverse{i}.txt", i-1)

        mult *= 10

def show_graph():
    pass

def main():
    evaluate_all(clustered_binary_insertion_sort, randomized_quick_sort)
    print(runtime_data)
    print(memory_data)

    runtime_data.clear()
    memory_data.clear()


main()