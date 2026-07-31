class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        def helper(isMax):
            prev=[-1]*n
            nex=[n]*n
            s=[]
            min_sum=0
            for i in range(n):
                if isMax:
                    while s and nums[s[-1]]>=nums[i]:
                        s.pop()
                else:
                    while s and nums[s[-1]]<=nums[i]:
                        s.pop()
                if s:
                    prev[i]=s[-1]
                s.append(i)
            s=[]
            for i in range(n-1,-1,-1):
                if isMax:
                    while s and nums[s[-1]]>nums[i]:
                        s.pop()
                else:
                    while s and nums[s[-1]]<nums[i]:
                        s.pop()

                if s:
                    nex[i]=s[-1]
                s.append(i)
            for i in range(n):
                l=i-prev[i]
                r=nex[i]-i
                min_sum+=nums[i]*l*r
        
            return min_sum
        
        return helper(False)-helper(True)