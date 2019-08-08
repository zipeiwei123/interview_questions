"""Use Graph
 Can use collections from python for highe performance
 """
# class Node:
#     def __init__(self, value = None):
#         self.value = value
#         self.neighbours = []
    
#     def add_value(self, value):
#         self.neighbours.append(value)

# class Graph:
#     def __init_(self):
#         self.number_of_nodes = {}
    
    
        

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #initial town judge
        number_of_town_judge = None
        #check for special conditions
        if not trust:
            return 0 
        """Iterate through the trust, append all the parent and child to graph"""
        graph = {}
        for relationship in trust:
            if relationship[0] not in graph:
                graph[relationship[0]] = [relationship[1]]
            else:
                graph[relationship[0]].append(relationship[1])
        
        #define by conditions
        # 1. town judge trust nobody
        for i in range(N+1):
            if i in graph and len(graph[i]) == 0:
                # a possible town judge
                number_of_town_judge = i
        
        # 2. others trust town judge
        for i in range(1,N+1):
            #except for the town judge
            if number_of_town_judge != i:
                if i in graph and number_of_town_judge not in graph[i]:
                    number_of_town_judge = -1
        
        
        #return number of judges
        return number_of_town_judge
                
            