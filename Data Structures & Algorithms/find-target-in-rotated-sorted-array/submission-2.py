class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        initialize left pointer
        right pointer
        middle
        while loop
        if the middle value is target:
            return index
        if left < middle and left < target:
            left = middle + 1
        else:
            right = middle - 1
        """
        l , r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: #if left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1