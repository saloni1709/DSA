class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)
        #         nums.append(i)
        # return nums


        ## BY TWO POINTER

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return l