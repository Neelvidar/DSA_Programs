#Search an Element: Write a program to accept N integers into an array and search for a given number.
#Display an appropriate message indicating whether the number is present in the array or not and also display its position.

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search_num = int(input("Enter the number to search: "))
found = False
for i in range(n):
    if arr[i] == search_num:
        print(f"Number found at position {i}")
        found = True
        break

if not found:
    print("Number not found in the array")