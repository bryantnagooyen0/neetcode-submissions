class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(numbers):
            rob1, rob2 = 0, 0
            for n in numbers:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            return max(helper(nums[1:]), helper(nums[:n - 1]))
        