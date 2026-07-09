class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maximum = max(candies)

        ans = []

        for candy in candies:
            if candy + extraCandies >= maximum:
                ans.append(True)
            else:
                ans.append(False)

        return ans


        