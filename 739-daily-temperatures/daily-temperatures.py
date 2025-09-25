class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        result=[0]*n
        stack=[]
        for i,j in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < j:
                prev=stack.pop()
                result[prev]=i-prev
            stack.append(i)
        return result


        