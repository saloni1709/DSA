class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0

        for i in nums:
            count = 0

            while i > 0:
                count += 1
                i = i // 10

            if count % 2 == 0:
                ans += 1
        
        return ans
