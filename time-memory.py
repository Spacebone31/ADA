import time
from memory_profiler import profile
from tabulate import tabulate
import psutil

def get_memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024  # Convert to megabytes

@profile
def find_mode_bruteforce(dataset):
    frequency_dict = {}

    for item in dataset:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    sorted_modes = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_modes

@profile
def find_mode_hashing(dataset):
    frequency_dict = {}

    for item in dataset:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    sorted_modes = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_modes

def measure_time_and_memory(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    memory_usage = get_memory_usage()
    return result, elapsed_time, memory_usage

# Example usage with grocery items:
small_dataset = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "banana"]
large_dataset = ["apple", "banana", "orange"] * 1000 + ["grape", "milk", "bread"] * 5000

# Measure time and memory for small dataset
result_small_bruteforce, time_small_bruteforce, memory_small_bruteforce = measure_time_and_memory(find_mode_bruteforce, small_dataset)
result_small_hashing, time_small_hashing, memory_small_hashing = measure_time_and_memory(find_mode_hashing, small_dataset)

# Measure time and memory for large dataset
result_large_bruteforce, time_large_bruteforce, memory_large_bruteforce = measure_time_and_memory(find_mode_bruteforce, large_dataset)
result_large_hashing, time_large_hashing, memory_large_hashing = measure_time_and_memory(find_mode_hashing, large_dataset)

# Calculate the difference in memory usage
memory_difference_small = memory_small_hashing - memory_small_bruteforce
memory_difference_large = memory_large_hashing - memory_large_bruteforce

# Print the results in a table
print("Comparison of Algorithms for Small Dataset:")
print(tabulate({
    "Algorithm": ["Bruteforce", "Hashing"],
    "Time (seconds)": [time_small_bruteforce, time_small_hashing],
    "Memory Usage (MB)": [memory_small_bruteforce, memory_small_hashing],
    "Memory Difference (MB)": [memory_difference_small, 0],
}, headers="keys", tablefmt="pretty"))

print("\nComparison of Algorithms for Large Dataset:")
print(tabulate({
    "Algorithm": ["Bruteforce", "Hashing"],
    "Time (seconds)": [time_large_bruteforce, time_large_hashing],
    "Memory Usage (MB)": [memory_large_bruteforce, memory_large_hashing],
    "Memory Difference (MB)": [memory_difference_large, 0],
}, headers="keys", tablefmt="pretty"))
