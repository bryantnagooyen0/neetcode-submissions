class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create frequency map and get frequency of every number
        get all items in the dictionary and put into an array [[frequency,num]]
        sort array by frequency
        get the k number of nums from end of array
        """
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        arr =[]
        for num, freq in freq_dict.items():
            arr.append([freq, num])

        sorted_arr = sorted(arr, key = lambda x: x[0], reverse = True)

        result = []
        for i in range(k):
            result.append(sorted_arr[i][1])
        return result
