"""Use Stack to keep check"""
class Solution:
    def isValid(self, s: str) -> bool:
#         stack = []
#         front = ("(", "[", "{")
#         back = (")", "]", "}")
        
#         for char in s:
#             if char in front:
#                 stack.append(char)
#             #check if stack not empty
#             elif char in back and stack:
#                 stack.remove(char)
#             else:
#                 back_tracking = "#"
        stack = []
        for symbol in s:
            if(symbol == "{" or symbol == "[" or symbol == "("):
                stack.append(symbol)
            elif(symbol == "}" and stack and stack[-1] == "{"):
                stack.pop()
            elif(symbol == "]" and stack and stack[-1] == "["):
                stack.pop()
            elif(symbol == ")" and stack and stack[-1] == "("):
                stack.pop()
            #if the above is not true, then it is not match up
            else:
                return False
        return True if not stack else False
                