class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n>>i) & 1 # getting every bit from n
            res = res | (bit << (31-i)) # placing that bit in the complimentary position in the result
     
        return res
        
