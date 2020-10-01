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
    def swap_pairs(self, head : ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next
        return head


def main():
    sol = Solution()

    l1 = LinkedList()
    l1.addAtTail(1)
    l1.addAtTail(2)
    l1.addAtTail(3)
    l1.addAtTail(4)
    l1.printList()

    start = time.time()
    res = LinkedList(sol.swap_pairs(l1.head.next))
    end = time.time()
    res.printList()
    print(end-start, " sec")


if __name__ == "__main__":
    main()





