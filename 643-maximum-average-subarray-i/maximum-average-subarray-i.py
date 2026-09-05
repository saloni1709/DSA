class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]
        max_sum = window_sum

        for j in range(k, len(nums)):
            window_sum -= nums[j-k]
            window_sum += nums[j]

            if window_sum > max_sum:
                max_sum = window_sum
        
        avg = max_sum / float(k)

        return avg
