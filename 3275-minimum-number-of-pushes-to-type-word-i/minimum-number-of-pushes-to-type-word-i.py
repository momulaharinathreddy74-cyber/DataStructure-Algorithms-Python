class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:
            return n
        c=n//8
        r=n%8
        res=0
        for i in range(c+1):
            res+=i*8
        res+=r*(c+1)
        return res
        