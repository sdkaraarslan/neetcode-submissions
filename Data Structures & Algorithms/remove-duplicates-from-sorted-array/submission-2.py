"""
Input:[] arr, increasingly sorted with duplicates in it

Output:[] without duplicates, return the length of [] which is "k"

Approach: 2 pointers

if pointers are the same, we dont move the p1. 

Input: nums = [2,10,30,30,30,30]
for                       i
p                         p


T.C. O(n)
S.C. O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for idx in range(1, len(nums)):
            if nums[idx] != nums[write-1]:
                nums[write]=nums[idx]
                write +=1
        return write



