class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for i in range(len(nums) + 1):
            dictionary[i] = 0
        
        for num in nums:
            dictionary[num] = 1
        
        for key, value in dictionary.items():
            if value == 0:
                return key
