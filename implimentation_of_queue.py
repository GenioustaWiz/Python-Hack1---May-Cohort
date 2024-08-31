class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, x: int) -> None:
        # Simply push the element onto stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, transfer all elements from stack1
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            raise IndexError("Queue is empty")
        
        # Return the top element from stack2
        return self.stack2.pop()

# Test the implementation
q = QueueWithStacks()
q.enqueue(167)
q.enqueue(900)
print(f"Dequeue Output 1: {q.dequeue()}")  # Output: 1
print(f"Dequeue Output 2: {q.dequeue()}")  # Output: 2

# Test empty queue
try:
    print(q.dequeue())
except IndexError as e:
    print(f"Dequeue Output 3: {str(e)}")  # Output: Queue is empty