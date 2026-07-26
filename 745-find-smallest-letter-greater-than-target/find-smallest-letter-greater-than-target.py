class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        l = 0
        r = len(letters) - 1
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if letters[mid] > target:
                ans = letters[mid]
                r = mid - 1
            
            else:
                l = mid + 1

        if ans == -1:
            return letters[0]
        
        return ans

            

            
        