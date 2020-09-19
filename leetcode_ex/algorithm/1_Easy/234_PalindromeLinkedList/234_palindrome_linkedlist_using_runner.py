import time
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode()

    def addAtTail(self, val):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = ListNode(val)

    def printList(self):
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
            print(curr_node.val, end=' ')
        print()


class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


def main():
    def determine(res: bool):
        if res == False:
            print("false : ", end-start, " sec")
        else:
            print("true : ", end-start, " sec")

    sol = Solution()
    l = LinkedList()
    l.addAtTail(1)
    l.addAtTail(2)
    l.printList()

    start = time.time()
    res = sol.is_palindrome(l.head)
    end = time.time()
    determine(res)

    l = LinkedList()
    l.addAtTail(1)
    l.addAtTail(2)
    l.addAtTail(2)
    l.addAtTail(1)
    l.printList()

    start = time.time()
    res = sol.is_palindrome(l.head)
    end = time.time()
    determine(res)


if __name__ == "__main__":
    main()
