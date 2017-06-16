#  542. 01 Matrix
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 5946
# Total Submissions: 18041
# Difficulty: Medium
# Contributors:
# Stomach_ache
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        row = len(matrix[0])
        col = len(matrix)
        # 0: not checed
        # 1: checked
        # 2: being checked
        checked = [[0 if matrix[j][i] else 1 for i in xrange(row)] for j in xrange(col)]
        for col_idx in xrange(col):
            for row_idx in xrange(row):
                if matrix[col_idx][row_idx] != 0 and not checked[col_idx][row_idx]:
                    matrix[col_idx][row_idx] = self.dfs(matrix, row_idx, col_idx, checked)
        # self.printMatrix(checked)

        return matrix

    def dfs(self, matrix, row, col, checked):
        # case 1: 0 return 0
        # case 2: 1 with neighbor 0 return 1
        # case 3: 1 with suround by 1s return min(dfs(top),dfs(left),dfs(left),dfs(right))
        if checked[col][row]:
            return matrix[col][row]

        neighbor = []
        if row > 0:
            neighbor.append(matrix[col][row - 1])
        if col > 0:
            neighbor.append(matrix[col - 1][row])
        if row < len(matrix[0]) - 1:
            neighbor.append(matrix[col][row + 1])
        if col < len(matrix) - 1:
            neighbor.append(matrix[col + 1][row])

        checked[col][row]= 1

        if 0 in neighbor:
            return 1
        else:
            res = []
            if row > 0:
                left = self.dfs(matrix, row - 1, col, checked)
                res.append(left)
            if col > 0:
                top = self.dfs(matrix, row, col - 1, checked)
                res.append(top)
            if row < len(matrix[0]) - 1:
                right = self.dfs(matrix, row + 1, col, checked)
                res.append(right)
            if col < len(matrix) - 1:
                bot = self.dfs(matrix, row, col + 1, checked)
                res.append(bot)
            return min(res)+1

    def printMatrix(self, matrix):
        print '=' * 20
        for row in matrix:
            print row


            # for dir in [(1,0),(0,1),(-1,0),(0,-1)]:
            #     dx, dy = dir
            #     nx, ny = i + dx, j + dy
            #     if nx >= 0 and ny>=0 and nx < len(matrix[0]) and ny < len(matrix):


if __name__ == '__main__':
    # input = [
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [1, 1, 1]
    # ]
    input = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]

    solver = Solution()
    solver.printMatrix(input)

    res = solver.updateMatrix(input)
    solver.printMatrix(res)
    solver.printMatrix([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]])

    # print Solution().updateMatrix(input)
