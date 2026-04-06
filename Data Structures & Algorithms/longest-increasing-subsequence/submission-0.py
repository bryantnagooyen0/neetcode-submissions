class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []
        count = 0

        def helper(subsequence, index):
            if index == len(nums):
                return len(subsequence)

            if not subsequence:
                new_sub = subsequence + [nums[index]]
                result = max(helper(subsequence, index + 1), helper(new_sub, index + 1))
                return result

            if index < len(nums) and nums[index] > subsequence[-1]:
                #Have the choice to skip number in index or append number to subsequence
                new_sub = subsequence + [nums[index]]
                result = max(helper(subsequence, index + 1), helper(new_sub, index + 1))
                return result
            else:
                return helper(subsequence, index + 1)
        
        return helper(subsequence, 0)

            

            

            
