class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        mid=''
        if n%2==0:
            mid=''
        else:
            mid=s[n//2]
        start=s[:n//2]
        sort=''.join(sorted(start))
        return sort[:]+mid+sort[::-1]