#Calculate Array Sum: Write a program to accept N integers into an array and 
#calculate and display the sum of all the elements. 

# Calculate Array Sum

n = int(input("Enter number of elements (N): "))

arr = []
print(f"Enter {n} integers:")
for i in range(n):
    num = int(input(f"Element {i+1}: "))
    arr.append(num)

total = sum(arr)

print("\nArray:", arr)
print("Sum of all elements:", total)
