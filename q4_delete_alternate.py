# Q4: Delete alternate nodes in the linked list (2nd, 4th, 6th, ...)

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

    def delete_alternate(self):
        temp = self.head
        while temp and temp.next:
            print(f"Deleting node with value {temp.next.data}")
            temp.next = temp.next.next
            temp = temp.next


ll = LinkedList()
n = int(input("How many nodes? "))
for i in range(n):
    ll.append(int(input(f"Enter value {i + 1}: ")))

print("\nOriginal list:")
ll.display()

print()
ll.delete_alternate()

print("\nList after deleting alternate nodes:")
ll.display()
