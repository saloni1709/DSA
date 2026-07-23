class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # even = []
        # odd = []

        # for i in nums:
        #     if i % 2 == 0:
        #         even.append(i)
        #     else:
        #         odd.append(i)
        # return even + odd


        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 != 0:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return nums
                
