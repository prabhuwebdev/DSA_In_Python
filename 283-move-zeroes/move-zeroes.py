class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left=0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left]=nums[i]
                left+=1
        for j in range(left,len(nums)):
            nums[j]=0
        

        
        
        