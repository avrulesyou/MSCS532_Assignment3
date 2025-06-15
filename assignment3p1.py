import random
import time
import matplotlib.pyplot as plt
import sys

# Adjust Python's recursion limit for the worst-case scenario in deterministic quicksort
sys.setrecursionlimit(20000)

def randomized_quicksort(arr):
    _r_quicksort(arr, 0, len(arr) - 1)

def _r_quicksort(arr, low, high):
    if low < high:
        pivot_index = _random_partition(arr, low, high)
        _r_quicksort(arr, low, pivot_index - 1)
        _r_quicksort(arr, pivot_index + 1, high)

def _random_partition(arr, low, high):
    rand_pivot_index = random.randint(low, high)
    arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]
    return _partition(arr, low, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr):
    _d_quicksort(arr, 0, len(arr) - 1)

def _d_quicksort(arr, low, high):
    if low < high:
        pivot_index = _deterministic_partition(arr, low, high)
        _d_quicksort(arr, low, pivot_index - 1)
        _d_quicksort(arr, pivot_index + 1, high)

def _deterministic_partition(arr, low, high):
    # Use first element as pivot by swapping it to the end for the partition function
    arr[low], arr[high] = arr[high], arr[low]
    return _partition(arr, low, high)

def generate_array(size, dist_type):
    if dist_type == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif dist_type == "sorted":
        return list(range(size))
    elif dist_type == "reverse_sorted":
        return list(range(size, -1, -1))
    elif dist_type == "repeated":
        return [random.randint(0, size // 10) for _ in range(size)]

def run_and_plot_analysis():
    sizes = [100, 500, 1000, 2500, 5000, 7500]
    distributions = ["random", "sorted", "reverse_sorted", "repeated"]
    
    fig, axs = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle('Randomized vs. Deterministic Quicksort Performance', fontsize=16)
    axs = axs.flatten()

    for i, dist in enumerate(distributions):
        print(f"--- Analyzing {dist.replace('_', ' ').title()} Arrays ---")
        det_times = []
        rand_times = []
        current_sizes = []

        for size in sizes:
            # Skip large sizes for deterministic on sorted data to avoid long run times
            if dist in ["sorted", "reverse_sorted"] and size > 2500:
                continue
            
            current_sizes.append(size)
            arr = generate_array(size, dist)

            det_arr = arr[:]
            start = time.perf_counter()
            deterministic_quicksort(det_arr)
            det_times.append(time.perf_counter() - start)

            rand_arr = arr[:]
            start = time.perf_counter()
            randomized_quicksort(rand_arr)
            rand_times.append(time.perf_counter() - start)
            
            print(f"Size: {size:<5} | Deterministic: {det_times[-1]:.5f}s | Randomized: {rand_times[-1]:.5f}s")
        
        ax = axs[i]
        ax.plot(current_sizes, det_times, 'o-', label='Deterministic (First Pivot)', color='red')
        ax.plot(current_sizes, rand_times, 's-', label='Randomized Pivot', color='blue')
        ax.set_title(f"Distribution: {dist.replace('_', ' ').title()}")
        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Execution Time (seconds)")
        ax.legend()
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    run_and_plot_analysis()