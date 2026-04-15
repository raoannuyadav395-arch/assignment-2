class DynamicArray:
    def __init__(self, capacity=2):
        self.n = 0  # Number of actual elements
        self.capacity = capacity # Max slots available [ 62]
        # We create a list of fixed size filled with None 
        self.A = [None] * self.capacity 

    def append(self, x):
        # If array is full, create a new array of double capacity [64]
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        
        self.A[self.n] = x # Insert new element at the next available slot [66]
        self.n += 1

    def _resize(self, new_cap):
        print(f"--- Resizing: {self.capacity} -> {new_cap} ---")
        # Create a new "plain list" for the larger capacity [ 51, 65]
        B = [None] * new_cap 
        
        # Copy elements to new array manually [65]
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B # Replace old array with the new one
        self.capacity = new_cap

    def pop(self):
        # Remove last element and return it [ 67]
        if self.n == 0: 
            return "Array is empty"
        val = self.A[self.n - 1]
        self.A[self.n - 1] = None # Clear the slot
        self.n -= 1
        return val

    def __str__(self):
        # Show only the elements currently in the array [ 68]
        return "[" + ", ".join(str(self.A[i]) for i in range(self.n)) + "]"





        # --- Task 1: Dynamic Array Test Cases ---
def test_dynamic_array():
    # 1. Start with small capacity as required 
    da = DynamicArray(capacity=2)
    print(f"Initial Capacity: {da.capacity}")

    # 2. Append 10+ items to show when resize happens 
    # The rubric checks for clean output showing size/capacity changes 
    for i in range(1, 11):
        old_cap = da.capacity
        da.append(i)
        if da.capacity > old_cap:
            print(f"Triggered Resize: Appended {i}, Capacity grew to {da.capacity}")
        else:
            print(f"Appended {i}: Current Array {da}")

    # 3. Perform 3 pops and show updated array
    print("\n--- Performing 3 Pops ---")
    for _ in range(3):
        popped_val = da.pop()
        print(f"Popped: {popped_val} | Current Array: {da}")

    print(f"Final State: {da} (Size: {da.n}, Capacity: {da.capacity})")

# Run the test
if __name__ == "__main__":
    test_dynamic_array()




print("==================================================================================================================")
# #tASK-2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Used for Doubly Linked List

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x) 
        new_node.next = self.head 
        self.head = new_node 

    def insert_at_end(self, x):
        new_node = Node(x) 
        if not self.head:
            self.head = new_node 
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node 

    def delete_by_value(self, x):
        curr = self.head 
        if curr and curr.data == x:
            self.head = curr.next 
            return
        prev = None
        while curr and curr.data != x:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next 

    def traverse(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(nodes) if nodes else "Empty List")

class DoublyLinkedList(SinglyLinkedList):
    def insert_after_node(self, target, x):
        curr = self.head 
        while curr and curr.data != target:
            curr = curr.next
        if curr:
            new_node = Node(x) 
            new_node.next = curr.next 
            new_node.prev = curr 
            if curr.next:
                curr.next.prev = new_node 
            curr.next = new_node 

    def delete_at_position(self, pos):
        # Using 0-based indexing as requested 
        if not self.head: return 
        curr = self.head
        if pos == 0:
            self.head = curr.next 
            if self.head: self.head.prev = None 
            return
        for _ in range(pos):
            if curr.next: curr = curr.next
        if curr.prev: curr.prev.next = curr.next 
        if curr.next: curr.next.prev = curr.prev 



def test_linked_lists():
    print("--- Task 2(A): Singly Linked List ---")
    sll = SinglyLinkedList()
    
    # Insert 3 at beginning, 3 at end 
    for i in [10, 20, 30]: sll.insert_at_beginning(i)
    for i in [40, 50, 60]: sll.insert_at_end(i)
    print("After insertions:")
    sll.traverse()

    # Delete one by value 
    sll.delete_by_value(20)
    print("After deleting 20:")
    sll.traverse()

    print("\n--- Task 2(B): Doubly Linked List ---")
    dll = DoublyLinkedList()
    for i in [1, 2, 3]: dll.insert_at_end(i)
    
    # Insert after a target
    dll.insert_after_node(2, 99) # Insert 99 after 2
    print("After inserting 99 after 2:")
    dll.traverse()

    # Delete at positions like 1 and last 
    dll.delete_at_position(1)
    print("After deleting at position 1:")
    dll.traverse()

# --- THE MAIN RUNNER ---
# This part actually executes your functions when i run the script.
if __name__ == "__main__":

    # This calls the Task 2 function i just defined
    test_linked_lists()


print("==================================================================================================================")
#task 3
class Stack:
    """Stack ADT (LIFO) using Singly Linked List storage [cite: 94]"""
    def __init__(self):
        self.storage = SinglyLinkedList()
        self.size = 0

    def push(self, x):
        # Insert at beginning for O(1) efficiency 
        self.storage.insert_at_beginning(x)
        self.size += 1

    def pop(self):
        # Remove from beginning for O(1) 
        if self.is_empty():
            print("Stack Underflow!")
            return None
        val = self.storage.head.data
        self.storage.head = self.storage.head.next
        self.size -= 1
        return val

    def peek(self):
        return self.storage.head.data if self.storage.head else None

    def is_empty(self):
        return self.size == 0

class Queue:
    """Queue ADT (FIFO) using Singly Linked List with Tail Pointer [cite: 100, 105]"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, x):
        # Add to tail for O(1) 
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        # Remove from head for O(1) 
        if self.is_empty():
            print("Queue Underflow!")
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val

    def front(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return self.size == 0
    
def test_stack_queue():
    print("\n--- Task 3(A): Stack Operations (LIFO) ---")
    s = Stack()
    s.push(10)
    s.push(20)
    print(f"Peek after pushing 10, 20: {s.peek()}") # Should be 20
    print(f"Popped: {s.pop()}") # Should be 20
    print(f"Stack empty? {s.is_empty()}")

    print("\n--- Task 3(B): Queue Operations (FIFO) ---")
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    print(f"Front after enqueuing A, B: {q.front()}") # Should be A
    print(f"Dequeued: {q.dequeue()}") # Should be A
    print(f"Queue empty? {q.is_empty()}")


if __name__ == "__main__":

    # This calls the Task 3 function i just defined
    test_stack_queue()



def is_balanced(expr):
    """
    Checks if an expression has balanced (), {}, and [] 122].
    Uses the custom Stack implementation from Task 3[ 118].
    """
    s = Stack()
    # Define matching pairs for easy lookup [ 122]
    matches = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        if char in "({[":
            # Push opening brackets onto the stack [ 119, 120]
            s.push(char)
        elif char in ")}]":
            # If stack is empty or top doesn't match, it's unbalanced [ 121]
            if s.is_empty() or s.pop() != matches[char]:
                return False
                
    # If the stack is empty at the end, all brackets were matched [ 120, 127]
    return s.is_empty()



def test_parentheses_checker():
    print("\n--- Task 4: Balanced Parentheses Checker ---")
    
    # Required test cases from the assignment [ 123]
    test_strings = {
        "([])": True,     # Balanced [ 124]
        "([)]": False,    # Not balanced [ 125]
        "(((": False,     # Not balanced [ 126]
        "": True          # Empty string is balanced [ 127]
    }
    
    for expr, expected in test_strings.items():
        result = is_balanced(expr)
        status = "Balanced" if result else "Not Balanced"
        print(f"Input: '{expr}' -> Result: {status} (Expected: {expected})")

if __name__ == "__main__":

    # This calls the Task 4 function i just defined
    test_parentheses_checker()