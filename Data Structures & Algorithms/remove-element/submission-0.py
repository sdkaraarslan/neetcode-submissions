"""
input____
nums []
int val

IN PLACE >> S.C. O(1)

output____
k = number of element left after removing all "val" ints from the array

approach_____
2-pointer
nums = [1,1,2,3,1,4,1], val = 1
        w
                    i
whenever idx is equal to val, we wont +1 to write 
whenever idx is not equal to val, we will +1 to write after writing current value to write

t.c.
s.c.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums:
            return 0
        write = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[write] = nums[idx]
                write+=1
        return write
