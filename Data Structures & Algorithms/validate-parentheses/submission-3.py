"""
INPUT

OUTPUT


APPROACH
the stack stores opening brackets that have not yet been closed.

s = "([{}])"
stack = "([{}])"


S.C. O(N)
T.C. O(N)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # opening brackets -> push to stack
            if char == "(":
                stack.append(char)
            elif char == "[":
                stack.append(char)
            elif char == "{":
                stack.append(char)

            # closing brackets -> must match the last opening one
            elif char == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop() #if in stack

            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop() #if in stack

            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop() #if in stack

        return len(stack) == 0