class Solution(object):
    def searchRange(self, nums, target):
        result=[]
        if not nums:
            return [-1,-1]
        if target not in nums:
            return [-1,-1]

        
        first_index=nums.index(target)
        result.append(first_index)

        last_index=len(nums)-1-nums[::-1].index(target)
        result.append(last_index)
        return result
        