class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Set=set(jewels)
        count=0
        for i in stones:
            if i in Set:
                count+=1
        return count
        