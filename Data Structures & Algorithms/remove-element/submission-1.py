"""
Input: nums = [1,1,2,3,4], val = 1
Output: [2,3,4]

Approach:
in-place, remove all occurrences of "val" in nums.
2 pointers

nums = [1,1,2,3,4], val = 1
        i
              p
        [1,2,3,3,4]


S.C.
T.C.
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        k=len(nums)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[write] = nums[i]
                write+=1 
            else:
                k-=1   
        return k