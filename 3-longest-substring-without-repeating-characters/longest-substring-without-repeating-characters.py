class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right=0
        left=0
        value={}
        max_length=0
        Max=[]
        while right <len(s):
            ch=s[right]
            while ch in value:
                value.pop(s[left])
                left+=1
            value[ch]=1
            max_length=max(max_length,right-left+1)
            right+=1
        
        return max_length
        