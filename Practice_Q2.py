# Find Largest, Second Largest, Smallest, Second Smallest

n = int(input("Enter number of elements (N): "))

arr = []
print(f"Enter {n} integers:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

unique_arr = list(set(arr))

if len(unique_arr) < 2:
    print("\nArray:", arr)
    print("Need at least 2 unique elements for second largest/smallest.")
else:
    unique_arr.sort()

    smallest = unique_arr[0]
    second_smallest = unique_arr[1]

    largest = unique_arr[-1]
    second_largest = unique_arr[-2]

    print("\nArray:", arr)
    print(f"Smallest element: {smallest}")
    print(f"Second smallest element: {second_smallest}")
    print(f"Largest element: {largest}")
    print(f"Second largest element: {second_largest}")