# 463. Island Perimeter
# Difficulty: Easy
# Contributors: amankaraj
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and
# there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't
# connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and
# height don't exceed 100. Determine the perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res += self.countEdge(grid,row,col)
        return res


    def countEdge(self,grid,row,col):
        edge = 0
        if row-1<0 or grid[row-1][col] == 0:
            edge += 1
        if col-1<0 or grid[row][col-1] == 0:
            edge += 1
        if row+1 == len(grid) or grid[row+1][col] == 0:
            edge += 1
        if col+1 == len(grid[0]) or grid[row][col+1] == 0:
            edge += 1
        return edge

if __name__ == '__main__':
    grid = [[1,0],[1,0]]
    print Solution().islandPerimeter(grid)