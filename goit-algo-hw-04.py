import timeit
import random


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


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def tim_sort(arr):
    arr.sort()


data = [random.random() for _ in range(100000)]

merge_time = timeit.timeit("merge_sort(data.copy())", globals=globals(), number=1)
insertion_time = timeit.timeit(
    "insertion_sort(data.copy())", globals=globals(), number=1
)
tim_time = timeit.timeit("tim_sort(data.copy())", globals=globals(), number=1)

print(f"{'| Algorothm' : <20} | {'Time data': <20} |")
print(f"|{'-'*19} | {'-'*20} |")
print(f"{'| Merge Sort': <20} | {merge_time:<20.5f} |")
print(f"{'| Insertion Sort': <20} | {insertion_time:<20.5f} |")
print(f"{'| Timsort': <20} | {tim_time:<20.5f} |")
