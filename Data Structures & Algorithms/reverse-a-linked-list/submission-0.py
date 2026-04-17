# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
2 pointers approach with a S.C. O(1) and T.C. of O(N)

(none) -> N1 ->  N2 ->  N3 -> N4..
  prev <- curr 
          prev <- curr 
                 prev <- curr 
          
          prev became the new curr
          curr became the new curr.next (temp)

  we should always swap curr.next with prev 
  (but to not break the linked list, keep next at temp pointer)

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
