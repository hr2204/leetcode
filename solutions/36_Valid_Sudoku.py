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
            for j in range(0,9):
                board[i][j]



        return True
    def helper(self,num,set):
        if num not in set:
            set.add(num)
            return
        else:
            return False
