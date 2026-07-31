class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        max1=float('-inf')
        l=0
        r=0
        se=set()
        while r<n:
            if s[r] not in se:
                se.add(s[r])
                r+=1
                max1=max(max1,r-l)
            else:
                se.discard(s[l])
                l+=1
        return max1