class Solution(object):
    def twoSum(self, nums, target):

        ## Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


        
        f = {}
        
        for i, val in enumerate(nums):
            required = target - val
            if required in f:
                return [f[required], i]
            
            f[val] = i