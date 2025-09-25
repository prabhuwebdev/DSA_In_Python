class Solution(object):
    def removeStars(self, s):
        result=[]
        for i in s:
            if i =="*" and result:
                result.pop()
            elif i != "*":
                result.append(i)
        return"".join(result)
        
        