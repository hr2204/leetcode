# 200. Number of Islands
# Difficulty: Medium
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        checked = []
        for i in range(len(grid)):
            checked.append([False] * len(grid[0]))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not checked[i][j]:
                    self.dfs(grid,i,j,checked)
                    res += 1
        return res

    def dfs(self,grid,i,j,checked):
        if i<len(grid) and j < len(grid[i]) and i>-1 and j > -1 and not checked[i][j] and grid[i][j] == "1":
            checked[i][j] = True
            self.dfs(grid,i+1,j,checked)
            self.dfs(grid,i,j+1,checked)
            self.dfs(grid,i-1,j,checked)
            self.dfs(grid,i,j-1,checked)


if __name__ == '__main__':
    grid = ["11110",
            "11010",
            "11000",
            "00000"]
    print Solution().numIslands(grid)