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

T.C. O(n^2)
S.C. O(n)
"""
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        answer = []
        for p1 in range(len(pairs)):
            p2 = p1 - 1
            while p2>=0 and pairs[p2].key > pairs[p2+1].key:
                pairs[p2], pairs[p2+1] = pairs[p2+1], pairs[p2]
                p2 -=1
            answer.append(pairs[:])
        return answer