import collections
class RecentCounter:

    def __init__(self):
        self.result=collections.deque()
        

    def ping(self, t: int) -> int:
        self.result.append(t)
        while self.result[0] < t-3000:
            self.result.popleft()
        return len(self.result)
         
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)