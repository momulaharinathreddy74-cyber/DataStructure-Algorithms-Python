class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min1=min(nums)
        max1=max(nums)
        ans=[]
        for i in range(min1,max1+1):
            if i not in nums:
                ans.append(i)
        return ans