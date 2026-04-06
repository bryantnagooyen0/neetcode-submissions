class MedianFinder:

    def __init__(self):
        #initialize small heap and large heap
        #small heap should be a max heap
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        """
        if there is large heap and number is larger than large[0], add to large heap
        else add it to small heap make sure to multiply by -1
        after we add number check if len of small heap > len(large) + 1
            if len is larger:
                get small[0] and push into large
        do same check for len(large)

        """
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1 * val)
            
        

    def findMedian(self) -> float:
        
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        return  ((-1 * self.small[0]) + self.large[0]) / 2.0
        
        
        