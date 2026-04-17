# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
i think of the recursion in two phases.

when i go down the recursive calls, i’m not changing links yet. 
i’m just walking deeper until i reach the new head, 
which is the last node. so the downward phase is basically discovery.

then, when the call stack unwinds and i come back up, 
that’s when the real work happens. 
each node uses the result from deeper recursion to flip one pointer. 
so if i had 1 -> 2 -> 3, once i reach 3, that becomes the new head.
 
then while returning:
3 <- 2
then 2 <- 1

so downward means ‘find the new head’,
upward means ‘reverse the direction of the links one by one

S.C. O(n)
T.C. O(n)
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
"""
[0,1,2,3]
last step: head(0).next = None
0 now head=0 but newHead is 3 and we need to make 1>0 so head.next(1).next=head(0) (DONE & DONE)
1 now head=1 but newHead is 3 and we need to make 2>1 so head.next(2).next=head(1) ^^^
2 now head=2 but newHead is 3 and we need to make 3>2 so head.next(3).next=head(2) ^^
3 returns newHead = 3 (DONE) ^


"""


        