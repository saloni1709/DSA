class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def firstOccurrence():
            l = 0
            r = len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    ans = mid
                    r = mid - 1
                
                elif nums[mid] < target:
                    l = mid + 1
                
                else:
                    r = mid - 1
            
            return ans

        def lastOccurrence():
            l = 0
            r = len(nums) - 1
            ans = -1

            while l <= r:
                mid = (l+r) // 2

                if nums[mid] == target:
                    ans = mid
                    l = mid + 1

                elif nums[mid] < target:
                    l = mid + 1

                elif nums[mid] > target:
                    r = mid - 1

                else:
                    return -1
        
            return ans
            
        first = firstOccurrence()
        last = lastOccurrence()

        return [first, last]
        
