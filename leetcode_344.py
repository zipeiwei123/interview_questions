"""Since it requires a O(1) in memory, use a tmp variable to swap"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #special condition, if not met
        if not s:
            return []
        else:
            s.reverse()
        """
        # a pointer to keep count the end of the string
        end = -1
        #iterate through in the middle of the string
        for start in range(0, int((len(s)+1)/2)):
            self.swap(s, start, end)
        return s
        
    def swap(self, s, start, end):
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        end -= 1
        """   