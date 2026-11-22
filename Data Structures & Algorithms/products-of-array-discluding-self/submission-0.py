class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=1
        new=[1]
        for i in range(1,len(nums)):
            right=nums[i-1]*left
            left=right
            new.append(right)
        
        temp=1
        for i in range(len(new)-1,-1,-1):
            new[i]*=temp
            temp*=nums[i]
        return new
        