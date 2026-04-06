class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Initialize rows and col
        initialize pacific and atlantic set

        def dfs(r,c,set,prev_height):
            validate r,c: if r < 0, c < 0, r >= ROWS, c >= COLS, if prev_height > new_height or in visited

            pacific_set.add((r,c))
            call function for 4 neighbor cells

        call it on all cells neighboring pacific
        call on cells neighboring atlantic

        check for cells in pacific and atlantic
        return those cells

        """

        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        res = []

        def dfs(r, c, visited, prev_height):
            #Validate r,c checking if cell is not in visited and is proper height for waterflow
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prev_height > heights[r][c] or (r, c) in visited:
                 return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for c in range(COLS):
            #Checking all cells at top row of pacific
            dfs(0, c, pacific, 0)

            #check all cells at bottom row of atlantic
            dfs(ROWS - 1, c, atlantic,0)

        for r in range(ROWS):
            dfs(r, 0, pacific, 0)

            dfs(r, COLS - 1, atlantic, 0)

        for r,c in pacific:
            if (r,c) in atlantic:
                res.append((r,c))
        return res


        
