"""It matters with combinations"""

class Solution:
    def romanToInt(self, s: str) -> int:
        lookup_table ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        symbols=['I','V','X','L','C','D','M']
        result=0
        if len(s)==1:
            return lookup_table[s[0]]
        else:
            for i in range(len(s)-1):
                if symbols.index(s[i]) < symbols.index(s[i+1]):
                    #IV
                    result -= lookup_table[s[i]]
                else:
                    result += lookup_table[s[i]]
        result += lookup_table[s[i+1]]
        return result