
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        hash1={}
        max1=0
        for i in range(len(fruits)):
            hash1[fruits[i]]=hash1.get(fruits[i],0)+1
            while len(hash1)>2:
                hash1[fruits[left]]-=1
                if hash1[fruits[left]]==0:
                    del hash1[fruits[left]]
                left+=1
            max1=max(max1,i-left+1)
        return max1

        
