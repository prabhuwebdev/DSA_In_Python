import collections
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds=0
        value=collections.deque((i,j) for i,j in enumerate(tickets))
        while value:
            a,b=value.popleft()
            if b>1:
                value.append((a,b-1))
                seconds+=1
            elif a == k and b == 1:
                seconds+=1
                break
            elif b == 1:
                seconds+=1
        return seconds