"""Determine if they have same number of each character"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #special condition, if s and t are both empty
        if not s and not t:
            return True
        #two dictionaries to store the string
        hash_one = {}
        hash_two = {}
        for s in s:
            if s not in hash_one:
                hash_one[s] = 1
            else:
                hash_one[s] += 1
        for s in t:
            if s not in hash_two:
                hash_two[s] = 1
            else:
                hash_two[s] += 1
                
        #check two hash table, if any of the condition is not met, return False
        for char in hash_one:
            if char not in hash_two or hash_one[char] != hash_two[char] or len(hash_one) != len(hash_two):
                return False
        return True