class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left , right = [1]*n , [1]*n
        res = []

        temp = 1
        for i in range(len(nums)):
            if i==0:
                left[i] = 1
                temp = nums[i]
            else:
                left[i] = temp
                temp *= nums[i]
        
        for i in range(n-1,-1,-1):
            if i == n-1:
                right[i] = 1
                temp = nums[i]
            else:
                right[i] = temp
                temp *= nums[i]
        
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res
