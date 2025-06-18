class SimpleStack:
    def init(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class SimpleQueue:
    def init(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


def check_palindrome(s):
    # Initialize stack and queue
    stack = SimpleStack()
    queue = SimpleQueue()

    # Push and enqueue each character
    for char in s:
        stack.push(char)
        queue.enqueue(char)

    # Compare characters from stack and queue
    is_palindrome = True
    while not stack.is_empty() and not queue.is_empty():
        stack_char = stack.pop()
        queue_char = queue.dequeue()
        if stack_char != queue_char:
            is_palindrome = False
            break

    # Output result
    if is_palindrome:
        print(f"The word, {s}, is a palindrome.")
    else:
        print(f"The word, {s}, is not a palindrome.")


# Read input
s = input().strip()

# Check constraints
if 1 <= len(s) <= 50:
    check_palindrome(s)
else:
    print("Invalid input: string length must be between 1 and 50.")