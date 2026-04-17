"""
INPUT

OUTPUT


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
        #to keep chars unclosed
        stack = []

        #to track what will be closed
        checklist = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        #we iterate over the string
        for char in s:
            if char in checklist:
                #were gonna return false if stack is empty or the char is unclosed
                if not stack or stack[-1] != checklist[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0


        
