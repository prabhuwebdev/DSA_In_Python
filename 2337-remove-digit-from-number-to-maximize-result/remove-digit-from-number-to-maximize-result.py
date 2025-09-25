class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        val=list(number)
        Count=val.count(digit)
        if Count == 1:
            val.remove(digit)
        else:
            for i in range(len(val)-1):
                if val[i] == digit and val[i] < val[i+1]:
                    val.pop(i)
                    break
            else:
                for i in range((len(val)-1),-1,-1):
                    if val[i] == digit:
                        val.pop(i)
                        break

        return "".join(val)
        