class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        first="".join(sorted(s))
        second="".join(sorted(t))
        hashmap[first]=s
        if second in hashmap.keys():
            return True 
        else:
            return False
        