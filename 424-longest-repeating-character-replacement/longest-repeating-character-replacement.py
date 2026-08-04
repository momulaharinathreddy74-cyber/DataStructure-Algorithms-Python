class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        hash1={}
        max1=0
        ans=0
        for i in range(len(s)):
            hash1[s[i]]=hash1.get(s[i],0)+1
            
            max1=max(max1,hash1[s[i]])
            while i-left+1-max1>k:
                hash1[s[left]]-=1
                if hash1[s[left]]==0:
                    del hash1[s[left]]
                left+=1
            ans=max(ans,i-left+1)
        return ans