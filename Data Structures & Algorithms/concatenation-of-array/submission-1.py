"""
S.C.
T.C.

Approach:

"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = 2 * [0] * len(nums)
        n=len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans