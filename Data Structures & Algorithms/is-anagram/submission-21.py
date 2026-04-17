"""
An anagram is a string that contains "the exact same characters" as another string, 
but the order of the characters can be different.
(we can track letters count and if theyre the same we can simply return True)

Input: s = "racecar", t = "carrace"
Output: true

Approach: 
since we cant track next chars without making T.C. higher, 
we should find a simpler approach instead if possible.
(we can use hashmap)

S.C. since we have to track each word I think this will make it O(m+n) automatically (assumption for now)
it is now O(n) since we loop for one's length
T.C. if we can track each word in one iteration for both and find the soln, we can make it O(m+n)
but basically O(n) if we use only english letters (26 chars only)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        #check if both are the same length, otherwise no need to check the rest anyways
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[s[i]] +=1
            count[t[i]] -=1

        return all(i==0 for i in count.values())

        