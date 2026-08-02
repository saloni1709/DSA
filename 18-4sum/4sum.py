class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        ans = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if i > 0 and nums[i] == nums[i-1]:
                    continue

                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l = j+1
                r = len(nums) - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

                    elif total < target:
                        l += 1
                    
                    else:
                        r -= 1

        return ans