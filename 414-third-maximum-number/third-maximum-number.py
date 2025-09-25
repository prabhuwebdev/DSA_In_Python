class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        value=sorted(set(nums))
        print(value)

        if len(value)>=3:
           return value[-3]
        else:
            return value[-1]
        