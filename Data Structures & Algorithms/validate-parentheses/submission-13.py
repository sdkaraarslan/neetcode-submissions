"""
Question:
'(', ')', '{', '}', '[',']'
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Approach:
Input: s = "()[]{}"

temp = [(]

create a dictionary of brackets sets,
iterate over the string, if the bracket is in the dictionary, add to temp, the next char if it closes the one in temp, keep checking

if closed >> pop from stack
if not closed >> return False

if all closed return True

S.C. O(n)
T.C. O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)  # if it opens, save it
            else:
                if stack and brackets[stack[-1]] == char:  # if last saved bracket matches this one
                    stack.pop()  # remove it because the pair is complete
                else:
                    return False  # wrong closing bracket or nothing to close

        return len(stack) == 0  # nothing should be left open

