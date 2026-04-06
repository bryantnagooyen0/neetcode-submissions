class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for i in range(32):
            bit = n & 1       # get last bit
            
            result = result << 1    # shift left
            
            result = result | bit    # add bit
            
            n = n >> 1          # shift right
        
        return result
        