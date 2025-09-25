class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        right=0
        Dict={}
        max_len=0
        while right < len(fruits):
            right_fruit=fruits[right]
            Dict[right_fruit]=Dict.get(right_fruit,0)+1
            while len(Dict) > 2:
                left_fruit = fruits[left]
                if left_fruit in Dict:
                    Dict[left_fruit]-=1
                    if Dict[left_fruit] == 0:
                        del Dict[left_fruit]
                left+=1
            max_len=max(max_len,right-left+1)
             
            right+=1
        return max_len