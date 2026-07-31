class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        visited = set()

        while n != 1:
            if n in visited:
                return False
            visited.add(n)

            sum = 0
            
            while n > 0:
                digit = n % 10
                sum += digit*digit
                n = n // 10

            n = sum
        
        return True