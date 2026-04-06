class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Hashmap
        iterate through the list
        for each number, add the difference as key to dictionary and the index as value

        """

        diff_dict = {}

        for index, num in enumerate(nums):
            diff = target - num
            if num in diff_dict:
                return [diff_dict[num], index]
            else:
                diff_dict[diff] = index

