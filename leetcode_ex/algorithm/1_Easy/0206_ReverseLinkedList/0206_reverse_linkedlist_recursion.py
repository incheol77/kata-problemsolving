import time
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def __init__(self, node=None):
        self.head = ListNode()
        self.head.next = node

    def addAtTail(self, val):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = ListNode(val)

    def printList(self):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            print(curr_node.val, end=" ")
        print()


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(curr: ListNode, prev: ListNode=None):
            if not curr:
                return prev
            next, curr.next = curr.next, prev
            return reverse(next, curr)
        return reverse(head.next)


def main():
    sol = Solution()

    l = LinkedList()
    l.addAtTail(1)
    l.addAtTail(2)
    l.addAtTail(3)
    l.addAtTail(4)
    l.addAtTail(5)

    start = time.time()
    res = LinkedList(sol.reverseList(l.head))
    end = time.time()
    res.printList()
    print(end-start, " sec")


if __name__ == "__main__":
    main()





