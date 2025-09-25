class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum=[0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_sum[0]=nums[i]
            else:
                prefix_sum[i]=prefix_sum[i-1]+nums[i]
        return prefix_sum
