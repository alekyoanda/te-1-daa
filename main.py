import time
import tracemalloc
from clustered_binary_insertion_sort import clustered_binary_insertion_sort

def read_data_file(filename):
    f = open(f"data/{filename}", "r")
    out = f.read()

    arr = out.split(",")
    f.close()

    return arr

def evaluate_time_and_space(func, filename):
    arr = read_data_file(filename)
    tracemalloc.start()
    start = time.time()
    func(arr)
    end = time.time()
    runtime = (end-start) * 1000
    malloc = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\t- {func.__name__} ({filename[:filename.find(".")-1]})")
    print(f"\t\tRuntime: {runtime}ms")
    print(f"\t\tMemory Allocation: {malloc}")

def main():
    print("SIZE 200:")
    evaluate_time_and_space(clustered_binary_insertion_sort, "sorted1.txt")
    evaluate_time_and_space(clustered_binary_insertion_sort, "random1.txt")
    evaluate_time_and_space(clustered_binary_insertion_sort, "reverse1.txt")

    print("\nSIZE 2000:")
    evaluate_time_and_space(clustered_binary_insertion_sort, "sorted2.txt")
    evaluate_time_and_space(clustered_binary_insertion_sort, "random2.txt")
    evaluate_time_and_space(clustered_binary_insertion_sort, "reverse2.txt")

    print("\nSIZE 20000:")
    evaluate_time_and_space(clustered_binary_insertion_sort, "sorted3.txt")
    evaluate_time_and_space(clustered_binary_insertion_sort, "random3.txt")
    evaluate_time_and_space(clustered_binary_insertion_sort, "reverse3.txt")

main()