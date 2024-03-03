from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T = None) -> None:
        self.next = None
        self.value = data

    def __str__(self) -> str:
        return "Node(next = {}, value = {})".format(self.next, self.value)


class Queue(Generic[T]):
    def __init__(self):
        self.start: Node | None = None
        self.end: Node | None = None
        self.elements: int = 0

    def push(self, data: T) -> None:
        newElement = Node(data)
        if self.elements < 1:
            self.start = newElement
            self.end = newElement
        else:
            self.end.next = newElement
            self.end = newElement
        self.elements += 1

    def pop(self) -> None:
        self.start = self.start.next
        self.elements -= 1

    def front(self) -> T:
        return self.start.value

    def size(self) -> int:
        return self.elements

    def empty(self) -> bool:
        return not self.size()


my_queue = Queue[int]()


my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
my_queue.push(4)


while my_queue.size():
    print(my_queue.front())
    my_queue.pop()
