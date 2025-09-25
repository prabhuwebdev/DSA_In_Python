class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        Stack=[]
        Value={}
        output=[]
        for i in nums2:
            while Stack and i >Stack[-1]:
                popped=Stack.pop()
                Value[popped]=i
            Stack.append(i)
            if i in Stack:
                Value[i]=-1
        for j in nums1:
            output.append(Value[j])
        return output

        
        