class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        """
        Create a frequency map
        frequency be the key, the integer be the value
        depending on k, return the k most frequent elements
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        freq_pairs = []
        for number, frequency in dict.items():
            freq_pairs.append((frequency,number))

        sorted_pairs = sorted(freq_pairs, reverse = True)

        result = []
        for i in range(k):
            result.append(sorted_pairs[i][1])
        return result



        
            