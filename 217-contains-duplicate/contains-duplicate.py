class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result={}
        for i in nums:
            if i in result: 
                return True
            result[i]=1
        return False
                


        