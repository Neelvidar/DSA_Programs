# Q1: Create a Singly Linear Linked List (append)

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


ll = LinkedList()
n = int(input("How many nodes? "))
for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    ll.append(value)
    print(f"Node {value} appended")

print("\nLinked list created successfully with", n, "nodes")
print("Head node value:", ll.head.data)
