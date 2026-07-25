class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        window_sum = 0
        count = 0

        for i in range(k):
            window_sum += arr[i]

        avg = window_sum / k
        if avg >= threshold:
            count += 1

        for j in range(k, len(arr)):
            window_sum -= arr[j-k]
            window_sum += arr[j]

            avg = window_sum / k

            if avg >= threshold:
                count+=1

        return count

        


        

        