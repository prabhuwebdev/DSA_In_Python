class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        right=0
        count=0
        vowels=set("aeiou")
        max_count=0
        while right < len(s):
            if s[right] in vowels:
                count+=1
            
            if right -left + 1 > k:
                 
                if s[left] in vowels:
                    count-=1
                left+=1
            if right - left + 1 == k:
                max_count=max(max_count,count)
            right+=1
        return max_count
        