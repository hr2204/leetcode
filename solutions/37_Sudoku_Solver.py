# 37. Sudoku Solver
# Difficulty: Hard
# Contributor: LeetCode
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#
#
# A sudoku puzzle...
# ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
# ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
#
# ...and its solution numbers marked in red.
#

class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def isValid(x,y):
            tmp=board[x][y]; board[x][y]='D'
            for i in range(9):
                if board[i][y]==tmp: return False
            for i in range(9):
                if board[x][i]==tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
            board[x][y]=tmp
            return True
        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j]=='.':
                        for k in '123456789':
                            board[i][j]=k
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i][j]='.'
                        return False
            return True
        dfs(board)
    def solveSudoku_Navie(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # print board

        ALL = set(['1','2','3','4','5','6','7','8','9'])

        map = {}
        for row in xrange(9):
            for col in xrange(9):
                if board[row][col] == '.':
                    map[(row,col)] = []

        # print map
        res = []
        preLen = 0
        flag = True
        while flag:
            flag = False
            for node in map:
                row, col = node
                self.regionHelp(board,row,col,map[node])
                self.rowHelper(board,row,map[node])
                self.colHelper(board,col,map[node])

            preLen = len(map.keys())

            for node in map:
                row, col = node
                if len(map[node]) == 8:
                    temp = list(board[row])
                    temp[col] = list(ALL - set(map[node]))[0]
                    board[row] = "".join(temp)
                    # board[row] = board[row][:col] + list(ALL - set(map[node]))[0] + board[row][col+1:]
                    flag = True



    def rowHelper(self,board,row,res):
        for i in xrange(9):
            if board[row][i] != '.' and board[row][i] not in res:
                res.append(board[row][i])

    def colHelper(self,board,col,res):
        for i in xrange(9):
            if board[i][col] != '.' and board[i][col] not in res:
                res.append(board[i][col])

    def regionHelp(self,board,row,col,res):
        dx = row/3
        dy = col/3
        for i in range(dx*3,dx*3+3):
            for j in range(dy*3,dy*3+3):
                if board[i][j] != '.' and board[i][j] not in res:
                    res.append(board[i][j])

    def showBoard(self,input):
        for row in input:
            temp = '|'
            for col in row:
                temp+= col + '|'
            print temp

if __name__ == '__main__':
    input = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    print Solution().showBoard(input)
    output = ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
    # print Solution().showBoard(output)

    Solution().solveSudoku(input)
    print Solution().showBoard(input)
