class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        for index, symbol in enumerate(s):
            if symbol in hash_table:
                #update with the second index number with an invalid char
                hash_table[index] = -1
            else:
                hash_table[index] = index
        return -1
    
        for key, value in hash_table.items():
            if value != -1:
                return key
        return  0