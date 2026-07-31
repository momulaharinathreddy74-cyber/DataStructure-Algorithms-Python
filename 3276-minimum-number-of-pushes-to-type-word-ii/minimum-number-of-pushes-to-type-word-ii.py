class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<9:
            return n
        hash12={}
        for w in word:
            if w not in hash12:
                hash12[w]=1
            else:
                hash12[w]+=1
        hash1={}
        for i in range(len(hash12)):
            val=max(hash12,key=hash12.get)
            if val not in hash1:
                d=len(hash1)//8
                hash1[val]=d+1
                del hash12[val]
            else:
                continue
        ans=0
        for w in word:
            ans+=hash1[w]
        return ans 