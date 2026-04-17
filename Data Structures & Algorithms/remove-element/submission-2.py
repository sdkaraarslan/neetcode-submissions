"""
in place: S.C. O(1)
          T.C. O(n)

           nums = [1,1,2,3,4], val = 1
                       r
                   w
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write +=1
        return write