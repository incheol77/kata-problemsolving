# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 1. linked list -> python list
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        
        # 2. sort python list
        lst.sort()
        
        # 3. python list -> linked list
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

