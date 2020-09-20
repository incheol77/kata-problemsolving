import collections
import time
from typing import Deque

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


def main():
    s = MyStack()
    for i in range(1, 4):
        s.push(i)
    print(s.top())
    print(s.empty())
    while not s.empty():
        print(s.pop(), end=' ')
        print(s.empty())
    print(s.empty())


if __name__ == "__main__":
    main()


