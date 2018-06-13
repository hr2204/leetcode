# 200. Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    self.dfs(grid, row, col)
                    ans += 1
        return ans

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0:
            return
        else:
            grid[row][col] = 0
            self.dfs(grid, row+1, col)
            self.dfs(grid, row, col+1)
            self.dfs(grid, row-1, col)
            self.dfs(grid, row, col-1)

if __name__ == '__main__':
    grid = [[1,1,0,0,0],
             [1,1,0,0,0],
             [0,0,1,0,0],
             [0,0,0,1,1]]

    # grid = [[1,1,1,1,0],
    #         [1,1,0,1,0],
    #         [1,1,0,0,0],
    #         [0,0,0,0,0]]
    sol = Solution()
    print sol.numIslands(grid)
