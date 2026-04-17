"""
Input: nums = [1, 2, 3, 3]
               p
                  i 

Output: true

Approach:

T.C. O(n)
S.C. O(n)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        check=set(nums)
        if len(nums)!= len(check):
            return True
        else:
            return False