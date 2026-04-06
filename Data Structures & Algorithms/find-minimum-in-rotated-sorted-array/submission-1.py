class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        initialize result
        initialize left and right

        while loop
            if array is sorted:
                set result and break

            initialize middle
            set result to min of middle and result
            if left is sorted:
                set left to past middle
            else:
                right to past middle
        return res
        """

        result = nums[0]
        l , r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result,nums[l])
                break
            
            m = (l + r) // 2

            result = min(result, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return result