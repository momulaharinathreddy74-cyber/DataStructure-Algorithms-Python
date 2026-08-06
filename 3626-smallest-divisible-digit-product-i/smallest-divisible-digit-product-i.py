class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        x=n
        while True:
            st=str(x)
            mul=1
            for s in st:
                mul=mul*(int(s))
            if mul%t==0:
                return x
            else:
                x=x+1
        