# Q3: Insert node at a specific position (1-based)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insert_at(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position {pos}")
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
        print(f"Inserted {data} at position {pos}")


ll = LinkedList()
n = int(input("How many nodes? "))
for i in range(n):
    ll.append(int(input(f"Enter value {i + 1}: ")))

print("\nList before insertion:")
ll.display()

val = int(input("\nEnter value to insert: "))
pos = int(input("Enter position (1-based): "))
ll.insert_at(val, pos)

print("\nList after insertion:")
ll.display()
