"""Use DFS, update equation and values to the graph
  graph [a] == set(b, 3.0)
  """

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #initial graph with graph set
        graph = collections.defaultdict(set)
        #create graph
        for numbers, value in zip(equations, values):
            x, y = numbers
            #add node in graph, each node has a set for corresponde node and value
            graph[x].add((y, value))
            graph[y].add((x, 1.0 / value))
        
        #create result
        results = []
        for query in queries:
            #get result for each query
            results.append(self.DFS(graph, query[0], query[1], set()))
            
        return results
        
        
    """Use recusrive to find correspondence value"""
    def DFS(self, graph, start, end, visited):
        #special case if a/a
        if start == end and graph[start]:
            return 1.0
        #append start node
        visited.add(start)
        #recursive through graph
        for neighbour, value in graph[start]:
            if neighbour in visited:
                continue
            #iterate through until find solution
            result = self.DFS(graph, neighbour, end, visited)
            if result > 0:
                return value * result
        return -1.0
        