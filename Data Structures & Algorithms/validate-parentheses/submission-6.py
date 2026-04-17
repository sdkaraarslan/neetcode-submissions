"""
INPUT
Input: s = "([{}])"

OUTPUT
true

APPROACH
the stack
it will store opening brackets that have not yet been closed

s = "([{}])"
stack = "([{}])"


S.C. O(N)
T.C. O(N)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checklist = {
            "}":"{",
            ")":"(",
            "]":"[",
        }

        for char in s:
            if char in checklist:
                if not stack or stack[-1] != checklist[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0