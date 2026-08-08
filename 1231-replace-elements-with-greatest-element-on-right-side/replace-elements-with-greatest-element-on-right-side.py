class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        # ans = []

        # for i in range(0, len(arr)):
        #     if i == len(arr)-1:
        #         ans.append(-1)
        #     else:
        #         right = arr[i+1:]
        #         ans.append(max(right))
        
        # return ans

        max_right = -1

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = max_right

            if curr > max_right:
                max_right = curr
        
        return arr

        