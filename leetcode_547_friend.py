"""Since it is a union find, use set to union find the number of friends"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        #first check special case
        if not M:
            return 0
        #initial number of friends
        number_of_friends = 0
        for i in range(len(M)):
            for j in range(len(M[i])):
                number_of_friends += self.find(i, j, M)
        
        return number_of_friends
    
    #The union find function that count number of friends
    def find(self, i, j, M):
        if i==j:
            
        
        #some condtions met when the friend are found
        return 1
        