# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
2 pointers >> S.C. O(1), T.C. O(n)

prev = head of reversed part
curr = head of remaining part

each step:
1) temp = curr.next   (save next)
2) curr.next = prev   (flip pointer)
3) prev = curr        (advance reversed head)
4) curr = temp        (advance forward)
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #initialize
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev=curr
            curr=temp
        return prev
