import timeit
import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def timsort(arr):
    arr.sort()


# Генеруємо випадковий масив для тестування
data_set = [random.randint(0, 1000) for _ in range(1000)]

# Вимірюємо час виконання алгоритмів
merge_sort_time = timeit.timeit(
    lambda: merge_sort(data_set.copy()), number=100)
insertion_sort_time = timeit.timeit(
    lambda: insertion_sort(data_set.copy()), number=100)
timsort_time = timeit.timeit(lambda: timsort(data_set.copy()), number=100)

# Виводимо результати
print(f"{'Algorithm': <20} | {'Dataset Time': <20}")
print(f"{'-' * 20} | {'-' * 20}")
print(f"{'Merge Sort': <20} | {merge_sort_time:<20.5f} ")
print(f"{'Insertion Sort': <20} | {insertion_sort_time:<20.5f} ")
print(f"{'Timsort': <20} | {timsort_time:<20.5f}")
