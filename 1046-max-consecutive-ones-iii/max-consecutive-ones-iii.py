class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0
        n=len(nums)
        l=0
        max1=float('-inf')
        for i in range(n):
            if nums[i]==0 :
                zeros+=1
            while zeros>k:
                if nums[l]==0:
                    zeros-=1
                l+=1
            max1=max(max1,i-l+1)
        return max1