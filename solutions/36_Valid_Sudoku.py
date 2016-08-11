# 36. Valid Sudoku
# Difficulty: Easy
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            numSet = set()
            for j in range(0,9):
                if board[i][j]!=".":
                    flag = self.helper(board[i][j],numSet)
                    if not flag:
                        return False

        for i in range(0,9):
            numSet = set()
            for j in range(0,9):
                if board[j][i]!=".":
                    flag = self.helper(board[j][i],numSet)
                    if not flag:
                        return False

        for i in range(0,3):
            for j in range(0,3):
                numSet = set()
                for m in range(0 + i * 3, 3 + i * 3):
                    for n in range(0 + j * 3, 3 + j * 3):
                        if board[m][n]!=".":
                            flag = self.helper(board[m][n],numSet)
                            if not flag:
                                return False


        return True
    def helper(self,num,set):
        if num not in set:
            set.add(num)
            return True
        else:
            return False


if __name__ == "__main__":
    testCase = ["....5..1.",
                ".4.3.....",
                ".....3..1",
                "8......2.",
                "..2.7....",
                ".15......",
                ".....2...",
                ".2.9.....",
                "..4......"]
    assert Solution().isValidSudoku(testCase) == False
