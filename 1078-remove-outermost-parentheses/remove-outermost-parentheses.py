class Solution(object):
    def removeOuterParentheses(self, s):
        result=[]
        count=0
        for i in s:
            if i == "(" and count ==0:
                count+=1
            elif i =="(" and count >0:
                result.append(i)
                count+=1
            elif i ==")":
                if count==1:
                    count-=1
                else:
                    count-=1
                    result.append(i)
        return "".join(result)