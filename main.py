from tabulate import tabulate

def find_mode(dataset):
    if len(dataset) < 10:  # Adjust the threshold as needed for your specific case
        return find_mode_bruteforce(dataset), find_mode_hashing(dataset)
    else:
        return find_mode_bruteforce(dataset), find_mode_hashing(dataset)

def find_mode_bruteforce(dataset):
    frequency_dict = {}

    for item in dataset:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    sorted_modes = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_modes

def find_mode_hashing(dataset):
    frequency_dict = {}

    for item in dataset:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    sorted_modes = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_modes

# Example usage with grocery items:
small_dataset = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "banana", "apple"]
large_dataset = ["apple", "banana", "orange"] * 1000 + ["grape", "milk", "bread", "apple"] * 5000

result_small_bruteforce, result_small_hashing = find_mode(small_dataset)
result_large_bruteforce, result_large_hashing = find_mode(large_dataset)

# Print the results in a table for small dataset
print("Mode for small dataset:")
print(tabulate({"Bruteforce": result_small_bruteforce, "Hashing": result_small_hashing}, headers="keys", tablefmt="pretty"))

# Print the results in a table for large dataset
print("\nMode for large dataset:")
print(tabulate({"Bruteforce": result_large_bruteforce, "Hashing": result_large_hashing}, headers="keys", tablefmt="pretty"))
