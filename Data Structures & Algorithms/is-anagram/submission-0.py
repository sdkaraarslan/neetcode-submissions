"""
Input: s = "racecar", t = "carrace"

Output: true

S.C.
T.C.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}

        for i in range(len(s)):
            char = s[i]
            if s[i] in count1:
                count1[char] +=1
            else:
                count1[char] = 1

        for i in range(len(t)):
            char = t[i]
            if t[i] in count2:
                count2[char] +=1
            else:
                count2[char] = 1

        return count1 == count2
