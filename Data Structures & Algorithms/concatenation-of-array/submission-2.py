"""
S.C. o(n)
T.C. o(n)

Approach: index mapping / offset-based writing

"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = 2 * [0] * n
        for i in range(len(nums)):
             ans[i] = nums[i]
             ans[i + n] = nums[i]
        return ans