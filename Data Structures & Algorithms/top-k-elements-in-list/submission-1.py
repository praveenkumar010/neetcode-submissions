class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        result=[]
        for i in range(len(nums)):
            seen[nums[i]]=seen.get(nums[i],0)+1
        for i,j in seen.items():
            if j>=k:
                result.append(i)
        return result
        