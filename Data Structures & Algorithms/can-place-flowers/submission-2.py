"""
3 cases: start, middle, end (start and end are edge cases, 
and we can deal with them as right and left side)
Input: flowerbed = [1,0,0,0,1], n = 2
left side >> flowerbed[0] or flowerbed[i-1]
right side >> flowerbed[len(flowerbed)-1] or flowerbed[i+1]

T.C. O(n)
S.C. O(1)
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            leftSide = (i == 0) or (flowerbed[i-1]==0)
            rightSide = (i == len(flowerbed)-1) or (flowerbed[i+1]==0)
            if flowerbed[i]==0 and leftSide and rightSide:
                count +=1
                flowerbed[i]=1
            if count>=n:
                return True
        return False