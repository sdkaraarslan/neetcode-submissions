"""
INPUT____
nums [] (len = n)


OUTPUT_____
create ans [] = 2*n
where ans[i] == nums[i] and 
      ans[i + n] == nums[i]
    
    return ans as the concat of two nums arr

APPROACH_____
nums = [1,4,1,2]
[1,4,1,2,1,4,1,2]
T.C.
S.C.


"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans = [[0] for _ in range(2*n)]

        for idx in range(len(nums)):
            ans[idx] = nums[idx]
            ans[idx+n] = nums[idx]
        return ans