class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total =  nums[0]
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]+1:
                total += nums[j]
            else:    
                break

        while total in nums:
            total += 1
        return total