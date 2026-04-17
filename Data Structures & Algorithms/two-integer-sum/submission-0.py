"""
Input: 
nums = [3,4,5,6], target = 7


Output: [0,1]

Approach:2 pointer approach

T.C.
S.C.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1, -1,-1):
            p = 0
            while p<i and nums[i] != target - nums[p]:
                p+=1
            if p<i and nums[i] == target - nums[p]:
                return [p,i]
