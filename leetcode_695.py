class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maximum_area = 0
        for r_index, row in enumerate(grid):
            for c_index, column in enumerate(row):
                if column != 0 and (r_index, c_index)  not in seen:
                    island_area = 0
                    stack = [(r_index, c_index)]
                    seen.add((r_index, c_index))
                    while stack:
                        r, c = stack.pop()
                        island_area += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    maximum_area = max(maximum_area, island_area)
        return maximum_area
                        
        #Use seen as a set to keep track the squares we haven't visited, and not count the same shape
        """Recusrively"""
#         seen = set()
#         return max(self.area(r, c, seen, grid) for r in range(len(grid)) for c in range(len(grid[0])))
    
    
#     def area(self, r, c, seen, grid):
#         if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
#                     and (r, c) not in seen and grid[r][c]):
#             return 0
#         seen.add((r, c))
#         return (1+self.area(r+1, c, seen, grid) + self.area(r-1, c, seen, grid) + self.area(r, c-1, seen, grid) + self.area(r, c+1, seen, grid))
        