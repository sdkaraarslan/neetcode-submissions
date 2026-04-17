"""
T.C. O(n)
S.C. O(1)

Approach:
arr = [2,4,5,3,1,2]

5 >> -1  >>-1
4 >> 2,-1 >>2
3 >> 1,2,-1 >>2
2 >> 3,1,2,-1 >>3
1 >> 5,3,1,2,-1 >>5
0 >> 4,5,3,1,2,-1 >>5

[5 5 3 2 2 -1]
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        for i in reversed(range(len(arr))):
            currNum = arr[i]
            arr[i] = maxRight
            maxRight = max(maxRight, currNum)
        return arr