class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Space in O(1)"""
        # #first solution bit manipulation
        # bit = 0
        # for number in nums:
        #     bit = bit ^ number
        # return bit
        """Space in O(N)"""
        l = []
        for number in nums:
            if number in l:
                l.remove(number)
            else:
                l.append(number)
        return l[0]