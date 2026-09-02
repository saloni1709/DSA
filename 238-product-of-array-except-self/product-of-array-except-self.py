class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prod = 1
        x = 1
        count = 0
        ans = []

        for i in nums:
            prod *= i
            if i == 0:
                count += 1
                continue
            else:
                x *= i

        for i in nums:
            if count > 1:
                ans.append(0)
            elif count == 1:
                if i == 0:
                    ans.append(x)
                else:
                    ans.append(0)
            else:
                ans.append(prod//i)
        
        return ans
