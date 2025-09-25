class Solution(object):
    def backspaceCompare(self, s, t):
        def compare(a):
            result=[]
            for i in a:
                if i == "#" and result:
                    result.pop()
                elif i !='#':
                    result.append(i) 
            return result
        return compare(s) == compare(t)    