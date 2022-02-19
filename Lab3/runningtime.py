import time
import random

random.seed()
n = 20000 # Size of array to sort
a = 1 # Lower bound of random integers to generate to populate array
b = 50000 # Upper bound

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        current = array[i]

        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current

arr = []
for i in range(1, n):
    arr.append(random.randint(a, b))

ti = time.time_ns()

print(arr)

print("\nWaiting on insertion sort...")
ti = time.time_ns()
insertion_sort(arr)
tf = time.time_ns()
runtime = (tf - ti) / 1e9

print(arr)
print(f"\nTime taken: {runtime} s")