class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        max_count = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
                
            if count > max_count:
                max_count = count
            
        return max_count