"""
T.C.non-decreasing order - no sort: o(n)
in place: S.C. O(1)
nums = [1,1,2,3,4]
          r
          w
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for read in range(1,len(nums)):
            if nums[read] == nums[write-1]:
                continue
            else:
                nums[write] = nums[read]
                write +=1
        return write

