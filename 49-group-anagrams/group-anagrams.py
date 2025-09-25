class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            s="".join(sorted(i))
            if s not in d:
                d[s]=[i]
            else:
                d[s].append(i)
        return (list(d.values()))
        