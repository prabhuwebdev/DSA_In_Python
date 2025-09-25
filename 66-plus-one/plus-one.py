class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value="".join(map(str,digits))
        digit=int(value)+1
        return [int(ch) for ch in str(digit)]