
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("List is empty")
        
        max_value = self.head.data
        current = self.head.next

        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value

# Test the implementation
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(5)
print(f"The maximum elements in the list is: {ll.find_max()}")  # Output: 5

# Test empty list
empty_ll = LinkedList()
try:
    print(empty_ll.find_max())
except ValueError as e:
    print(str(e))  # Output: List is empty