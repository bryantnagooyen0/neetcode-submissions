class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[3,4,5,6,1,2]
        #[0,1,2,3,4,5] indexes

        left = 0
        right = len(nums) - 1

        res = nums[0]
        while left <= right:
            
            if nums[left] < nums[right]:
                return min(res, nums[left])
                break

            m = (left + right) // 2
            res = min(res, nums[m])
                #if left is < middle num then we take right section else take left
            if nums[left] <= nums[m]:
                left = m + 1
            else:
                right = m - 1
        return res
                
            




            
            
        