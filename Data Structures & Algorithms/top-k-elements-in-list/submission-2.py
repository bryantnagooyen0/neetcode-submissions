class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create frequency map of elements and frequency
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        #sort map by frequency

        nums_sorted = sorted(freq.items(), key=lambda item:item[1],reverse = True)
        #return top k elements through for loop
        result = []
        for i in range(k):
           result.append(nums_sorted[i][0])
        return result

