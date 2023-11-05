import numpy as np
import timeit
import matplotlib.pyplot as plt
import tracemalloc
from clustered_binary_insertion_sort import clustered_binary_insertion_sort
from randomized_quick_sort import randomized_quick_sort

SIZE = [200, 2000, 20000]
DATA_TYPE = ["Sorted", "Random", "Reverse"]
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
    arr = read_data_file(filename)
    tracemalloc.start()
    start = timeit.default_timer()
    # print("before", arr)
    func(arr)
    # print("after", arr)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = timeit.default_timer()
    runtime = (end-start) * 1000
    runtime = float("%.3f" % runtime)
    
    
    print(f"\t\t{func.__name__}")
    print(f"\t\t\tRuntime: {runtime} ms")
    print(f"\t\t\tMemory Allocation: {peak} bytes")

    return runtime, peak

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
    for i in range(len(SIZE)):
        size_200_1 = memory_data[0][i]
        size_200_2 = memory_data[1][i]

        max_value = max(max(size_200_1), max(size_200_2))

        dict_200 = {
            "CBIS": size_200_1,
            "Random Quick Sort": size_200_2
        }
        # plot line 
        x = np.arange(len(SIZE))  # the label locations
        width = 0.4  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in dict_200.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Memory Usage (bytes)')
        ax.set_title(f'Input Size {SIZE[i]}')
        ax.set_xticks(x + width, DATA_TYPE)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, max_value * 1.1)

        plt.savefig(f'figure/memory_{SIZE[i]}.png')
        plt.show()

def main():
    evaluate_all(clustered_binary_insertion_sort, randomized_quick_sort)
    # print(runtime_data)
    # print(memory_data)

    # uncomment baris kode di bawah ini untuk generasi graph baru
    # show_graph() 

main()