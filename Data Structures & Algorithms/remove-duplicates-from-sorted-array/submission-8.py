
"""
Approach: 2 pt
nums = [1,1,2,3,4]
          w
          r

S.C.
T.C.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for read in range(1,len(nums)):
            if nums[write-1]!= nums[read]:
                nums[write]=nums[read]
                write+=1
        return write