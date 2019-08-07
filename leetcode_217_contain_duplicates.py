"""Use hash table to keep check each number in nums 's independent'"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash_table = {}
        # for number in nums:
        #     if number in hash_table:
        #         hash_table[number] += 1
        #     else:
        #         hash_table[number] = 1
        # for number, frequency in hash_table.items():
        #     if frequency > 1:
        #         return True
        # return False
        #Second way
        hash_t = []
        for number in nums:
            if number in hash_t:
                return True
            else:
                hash_t.append(number)
        return False
                