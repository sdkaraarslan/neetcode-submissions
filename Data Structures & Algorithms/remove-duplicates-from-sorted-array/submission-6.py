"""
Input:[] 
arr, increasingly sorted with duplicates in it

Output:[] 
without duplicates, 
return the length of [] => "k" INPLACE CHANGE 

Approach: 2 pointers

if pointers are the same, we dont move the p1. 
we keep write as +1 to keep the right idx to correct.

Input: nums = [2,10,30,30,30,30,40]
for                    i
write                  w
Input: nums = [2,10,30,40,...]

if the idx is equal to the idx one before, we will keep write as it is
if the idx is NOT equal to the idx one before, we do write +=1

T.C. O(n)
S.C. O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        write = 0
        scan = 0

        while scan < n:
            nums[write] = nums[scan]   # write the new unique value

            # skip all duplicates of this value
            while scan < n and nums[scan] == nums[write]:
                scan += 1

            write += 1

        return write