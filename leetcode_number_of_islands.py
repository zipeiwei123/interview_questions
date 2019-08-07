"""A question regarding DFS with backtracking. However, I also like to view it as a solution to DP, by breaking the questions into subproblem
    1 1 0
    0 1 1
    1 1 0"""
"""Consider index(1,1), what is its neighbours, iterate through all the indexes in grid"""
"""Running Time O(N*N)"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #check for normal case
        if grid:
            #initial variable for counting number of islands
            number_of_islands = 0
            #iterate through all the indexes
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    #we only interested in island == "1"
                    if grid[i][j] == "1":
                        number_of_islands += self.dfs_backtracking(grid, i, j)
            #return number of islands
            return number_of_islands
        
        #first check special case
        else:
            return 0
    """DFS with backtracking needs to watch out for the visited matrix/stack"""
    
    def dfs_backtracking(self, grid, i, j):
        #stop condition, check for inbound/outbound, or island not found
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0":
            return 0
               
        #set current as visited
        grid[i][j] = "0"
        #revisited left right top down
        self.dfs_backtracking(grid, i+1, j)
        self.dfs_backtracking(grid, i-1, j)
        self.dfs_backtracking(grid, i, j+1)
        self.dfs_backtracking(grid, i, j-1)
        return 1