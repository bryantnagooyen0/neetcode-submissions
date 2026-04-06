class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        result = 0
        mask = 0xffffffff

        for i in range(32):
            #calc a and b bit
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            #XOR a_bit, b_bit, and carry into result at correct location
            result = result | (a_bit ^ b_bit ^ carry) << i

            #calculate carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
        
        if result >= 2**31:
            result -= 2**32
                

        return result

