"""Keep checking until reached the end"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # #2^0 = 1
        # maximum = 1
        # while maximum < n:
        #     maximum = maximum *2
        # if maximum == n:
        #     return True
        # else:
        #     return False
        return n > 0 and (math.log10(n) / math.log10(2)).is_integer()