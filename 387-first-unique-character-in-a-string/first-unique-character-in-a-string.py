class Solution:
    def firstUniqChar(self, s: str) -> int:
        result={}
        for ch in s:
            if ch in result:
                result[ch]+=1
            else:
                result[ch]=1
        for i,ch in enumerate(s):
            if result[ch] == 1:
                return i
        return -1
