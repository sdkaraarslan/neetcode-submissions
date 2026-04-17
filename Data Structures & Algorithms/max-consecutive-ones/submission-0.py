"""
Approach: 
we iterate once through the array, 
maintain a running count of consecutive 1s, 
reset on 0, and track the maximum seen so far

S.C. O(1)
T.C. O(N)

follow-up they might ask
“what if you can flip at most one 0?”

that becomes:
-sliding window
-allow one zero inside window
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currCount = 0
        for num in nums:
            if num == 1:
                currCount+=1
            else:
                currCount = 0
                
            maxCount = max(currCount, maxCount)
        return maxCount
            