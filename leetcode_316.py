class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        orders = [('a',2), ('b',3), ('c',4)]
        #orders = ["a", "b", "c"]
        l = []
        for char in s:
            if char not in l:
                l.append(char)
        l.sort(key = lambda i: for i, j in orders)
        str1 = ''.join(l)
        return str1