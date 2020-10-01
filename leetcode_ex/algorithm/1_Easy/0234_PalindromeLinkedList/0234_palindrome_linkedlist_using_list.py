import time
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = ListNode()

    def addAtTail(self, val):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def printNode(self):
        curr = self.head
        while curr.next:
            curr = curr.next
            print(curr.val)


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        q: List = []
        node = head.next
        if not node:
            return True
        while node is not None:
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True


def main():
    def determine(res):
        if res == False:
            print("false : ", end - start, " sec")
        else:
            print("true : ", end - start, " sec")

    l = LinkedList()
    l.addAtTail(1)
    l.addAtTail(2)
    sol = Solution()
    start = time.time()
    res = sol.is_palindrome(l.head)
    end = time.time()
    determine(res)

    l = LinkedList()
    l.addAtTail(1)
    l.addAtTail(2)
    l.addAtTail(2)
    l.addAtTail(1)
    start = time.time()
    res = sol.is_palindrome(l.head)
    end = time.time()
    determine(res)

if __name__ == "__main__":
    main()
