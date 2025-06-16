class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n <= 0:
            raise IndexError("Index must be 1 or greater.")
        if n == 1:
            self.head = self.head.next
            return
        current = self.head
        count = 1
        while current and count < n - 1:
            current = current.next
            count += 1
        if not current or not current.next:
            raise IndexError("Index out of range.")
        current.next = current.next.next

try:
    ll = LinkedList()
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial list:")
    ll.print_list()

    print("\nDeleting 2nd node...")
    ll.delete_nth_node(2)
    ll.print_list()

    print("\nDeleting 1st node...")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nDeleting node at index 5 (out of range)...")
    ll.delete_nth_node(5)

except Exception as e:
    print("Error:", e)
