# Q5: Complete program - all 4 operations together

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list (append)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 2. Traverse and print
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # 3. Insert at position
    def insert_at(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                break
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        new_node.next = temp.next
        temp.next = new_node

    # 4. Delete alternate nodes
    def delete_alternate(self):
        temp = self.head
        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next


ll = LinkedList()

# 1. Create
n = int(input("How many nodes? "))
for i in range(n):
    ll.append(int(input(f"Enter value {i + 1}: ")))
print("\n1. Linked list created (append):")
ll.display()

# 2. Traverse
print("\n2. Traversal of linked list:")
ll.display()

# 3. Insert
val = int(input("\nEnter value to insert: "))
pos = int(input("Enter position (1-based): "))
ll.insert_at(val, pos)
print(f"\n3. After inserting {val} at position {pos}:")
ll.display()

# 4. Delete alternate
ll.delete_alternate()
print("\n4. After deleting alternate nodes:")
ll.display()
