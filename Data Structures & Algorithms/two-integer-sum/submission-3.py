"""
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]

Approach:
hashmap
[3,4,5,6]
1)need = 7-3=4(is it in the hashmap?) 

3)     {3:0} (if not add the value to hashmap), how?
        checklist[nums[i]]=i


2)check until you find the value in hashmap
need = 7-4=3(is it in the hashmap?) 
yes, bring the value of key 3 >> checklist[need]

T.C.
S.C.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checklist = {} #what number would i need to add to THIS one to reach the target?”
        for i, n in enumerate(nums):
            need = target - n
            if need in checklist:
                return [checklist[need],i]
            checklist[n]=i
            
            
