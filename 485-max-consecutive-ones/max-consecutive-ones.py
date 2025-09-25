class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        result=[]
        for i in nums:
            if i == 1:
                count+=1
            else:
                result.append(count)
                count=0
        result.append(count)
        return max(result)
        
        