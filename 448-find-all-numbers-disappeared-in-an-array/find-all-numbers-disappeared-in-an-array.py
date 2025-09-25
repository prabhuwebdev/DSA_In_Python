class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        for i in nums:
            pos=abs(i)-1
            if nums[pos]>0:
                nums[pos]*=-1
        for j in range(len(nums)):
            if nums[j] >0:
                result.append(j+1)
        return result
        