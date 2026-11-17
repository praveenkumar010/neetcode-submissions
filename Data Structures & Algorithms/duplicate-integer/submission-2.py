class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=max(nums)
        res=(n*(n+1)/2)
        if sum(nums)==res:
            return False
        else:
            return True
