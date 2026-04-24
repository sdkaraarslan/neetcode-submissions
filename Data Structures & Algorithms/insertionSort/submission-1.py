# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

"""
approach: Insertion Sort (build order gradually)

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
                          p1 
           p2
Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]] 

j = 2
# current item is 1
[5, 2, 1]
       j

[5, 1, 2]
    j? > j-=1

T.C. O(n^2)
S.C. O(n)
"""
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        answer = []
        for i in range(len(pairs)):
            j = i-1
            while j>=0 and pairs[j].key > pairs[j+1].key:
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1] 
                j -=1
            answer.append(pairs[:])
        return answer
