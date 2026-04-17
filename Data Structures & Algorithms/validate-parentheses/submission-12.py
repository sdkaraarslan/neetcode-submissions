"""
T.C.
S.C.

approach
Input: s = "([{}])"
we have some word, if this word has these chars, then we need to keep them somewhere
which is
checkArray = [ (,[,{ ]
but we do so by checking the last element (if exists) in the array,
if this element is closed, thats fine we pop that one, if not we return False.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        checkStack = []
        checklist = {
            "]":"[",
            "}":"{",
            ")":"(",
        }

        for char in s:
            if checkStack and char in checklist:
                if checkStack[-1] != checklist[char]:
                    return False
                else:
                    checkStack.pop()
            #if char is not in checkStack yet
            else:
                checkStack.append(char)
        return len(checkStack)==0
            
                    

