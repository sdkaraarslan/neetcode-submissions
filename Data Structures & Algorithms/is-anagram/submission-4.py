"""
Input: s = "racecar", t = "carrace"

Output: true

S.C. O(n+m)
T.C. O(n+m)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)

        if len(counter1) != len(counter2):
            return False

        for k, v in counter1.items():
            if counter2[k] != v:
                return False
        

        return True
