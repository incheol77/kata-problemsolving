import collections

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


def main():
    q = MyQueue()
    for i in range(1, 4):
        q.push(i)
        print(q.peek(), end=' ')
    print()
    for i in range(1, 4):
        print(q.pop(), end=' ')


if __name__ == "__main__":
    main()
