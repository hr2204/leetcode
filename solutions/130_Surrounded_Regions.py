# 130. Surrounded Regions  QuestionEditorial Solution  My Submissions
# Total Accepted: 63014
# Total Submissions: 373374
# Difficulty: Medium
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

class Solution(object):

    def solve_BFS(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def fill(x, y):
            if x < 0 or x > m - 1 or y < 0 or y > n - 1 or board[x][y] != 'O':
                return
            queue.append((x, y))
            board[x][y] = 'D'

        def bfs(x, y):
            if board[x][y] == 'O':
                fill(x, y)
            while queue:
                cur = queue.pop(0)
                i = cur[0]
                j = cur[1]
                fill(i + 1, j)
                fill(i - 1, j)
                fill(i, j + 1)
                fill(i, j - 1)

        if len(board) == 0:
            return
        m = len(board)
        n = len(board[0])
        queue = []

        for i in range(n):
            bfs(0, i)
            bfs(m - 1, i)
        for j in range(1, m - 1):
            bfs(j, 0)
            bfs(j, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    # max recursion depth excced
    def solve_DFS(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        checked = []
        for i in range(len(board)):
            checked.append([False] * len(board[i]))
        print checked

        for i in range(len(board[0])):
            self.dfs(board,checked,0,i)
        for i in range(len(board[0])):
            self.dfs(board,checked,len(board)-1,i)
        for i in range(len(board)):
            self.dfs(board,checked,i,0)
        for i in range(len(board)):
            self.dfs(board,checked,i,len(board[i])-1)

        for i in range(len(board)):
            temp = ""
            for j in range(len(board[i])):
                if checked[i][j]:
                    temp += "O"
                else:
                    temp += "X"
            board[i] = temp

    def dfs(self,board,checked,i,j):
        if board[i][j] == "O" and not checked[i][j]:
            checked[i][j] = True
            if i < len(board) - 1:
                self.dfs(board,checked,i+1,j)
            if j < len(board[i]) - 1:
                self.dfs(board,checked,i,j+1)
            if i > 0:
                self.dfs(board,checked,i-1,j)
            if j > 0:
                self.dfs(board,checked,i,j-1)

if __name__ == '__main__':
    grid = ["OO","OO"]
    Solution().solve(grid)
    for row in grid:
        print row