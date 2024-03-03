class Node:
    def __init__(self, data=None):
        self.next = None
        self.value = data

    def __str__(self):
        return "Node(next = {}, value = {})".format(self.next, self.value)


class Stack:
    def __init__(self):
        self.curr = Node()
        self.elements = 0

    def push(self, data):
        newElement = Node(data)
        newElement.next = self.curr.next
        self.curr.next = newElement
        self.elements += 1

    def pop(self):
        self.elements -= 1
        self.curr.next = self.curr.next.next

    def top(self):
        element = self.curr.next
        return element.value

    def size(self):
        return self.elements

    def empty(self):
        return not self.size()


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)


while not my_stack.empty():
    print(my_stack.top())
    my_stack.pop()
