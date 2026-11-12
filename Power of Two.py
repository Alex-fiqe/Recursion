class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if 2**i == n:
                i+=1
                return True
            
        return False
