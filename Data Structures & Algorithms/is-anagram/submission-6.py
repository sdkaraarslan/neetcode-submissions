"""
Input: s = "racecar", t = "carrace"

Output: true

S.C. O(n+m)
T.C. O(n+m)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(s)):
            char = s[i]
            count1[char] +=1
            

        for i in range(len(t)):
            char = t[i]
            count2[char] +=1
           

        return count1 == count2

