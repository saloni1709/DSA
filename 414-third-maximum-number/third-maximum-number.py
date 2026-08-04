class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # nums = list(set(nums))
        # for i in range(len(nums)):
        #     nums.sort(reverse = True)
        #     if len(nums) < 3:
        #         return max(nums)
        # return nums[2]

        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

       

        