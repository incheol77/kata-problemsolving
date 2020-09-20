import time
from typing import List

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
        self.length = 0

    def push(self, item):
        self.last = Node(item, self.last)
        self.length += 1

    def pop(self) -> Node:
        item = self.last.item
        self.last = self.last.next
        self.length -= 1
        return item

    def len(self):
        return self.length


def main():
    s = Stack()
    for i in range(1, 6):
        s.push(i)
    for _ in range(s.len()):
        print(s.pop())


if __name__ == "__main__":
    main()

