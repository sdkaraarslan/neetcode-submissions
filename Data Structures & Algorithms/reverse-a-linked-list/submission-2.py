# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
S.C.
T.C.

Approach: 2 pointers
head = [0,1,2,3]
        <-
           <-
              <-
prev = None
curr = head

[None,next] -> [val1,next] ....-> [val2,next] -> [val3,next] ...
 prev           curr               curr.next
                curr.next->None.   no longer the curr.next(so we need to save this)
 
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev #(at the end curr end up at None while prev in the last value)