class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        

        for i in range(len(nums) - 2, -1, -1):
            end = min(n, nums[i] + i + 1)
            for j in range(i, end):
                if dp[j] == True:
                    dp[i] = True
        return dp[0]
            
    #i = 1
    #end = 4
    #


