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
            print(curr_node.val, end="->")
        print()


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return head.next


def main():
    sol = Solution()

    l1 = LinkedList()
    l1.addAtTail(2)
    l1.addAtTail(4)
    l1.addAtTail(3)
    l1.printList()

    l2 = LinkedList()
    l2.addAtTail(5)
    l2.addAtTail(6)
    l2.addAtTail(4)
    l2.printList()

    start = time.time()
    res = LinkedList(sol.add_two_numbers(l1.head.next, l2.head.next))
    end = time.time()
    res.printList()
    print(end-start, " sec")


if __name__ == "__main__":
    main()





