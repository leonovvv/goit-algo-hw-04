from timeit import timeit
import random

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Набори даних для тестування
def generate_random_list(size):
    return random.sample(range(size*10), size)

# Функція для вимірювання часу
def measure_time(algorithm, arr):
    return timeit(lambda: algorithm(arr.copy()), number=1)

# Основна функція для порівняння алгоритмів
def compare_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]  # Різні розміри масивів
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Timsort": sorted
    }

    print(f"{'Algorithm':<20} {'Size':<10} {'Time (s)':<10}")
    print("-" * 40)

    for size in sizes:
        arr = generate_random_list(size)
        for name, algorithm in algorithms.items():
            time_taken = measure_time(algorithm, arr)
            print(f"{name:<20} {size:<10} {time_taken:<10.6f}")

if __name__ == "__main__":
    compare_sorting_algorithms()
