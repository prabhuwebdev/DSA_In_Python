class Solution(object):
    def isValid(self, s):
        stack=[]
        pair={
            ")":"(",
            "}":"{",
            "]":"["
        }
        openings=set(pair.values())
        for i in s:
            if i in openings:
                stack.append(i)
            else:
                if not stack:
                    return False
                if pair[i] == stack[-1]:
                    stack.pop()
                elif pair[i] != stack[-1]:
                    return False
        return not stack
    
        