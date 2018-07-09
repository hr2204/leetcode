# 79. Word Search
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) > len(board) * len(board[0]):
            return False
        checked = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.helper(board, row, col, word, 0, checked):
                    return True

        return False

    def helper(self, board, row, col, word, index, checked):

        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return False

        if checked[row][col] or board[row][col] != word[index]:
            return False

        if board[row][col] == word[index] and index == len(word) - 1:
            return True

        checked[row][col] = True

        res = self.helper(board, row + 1, col, word, index + 1, checked) or \
              self.helper(board, row, col + 1, word, index + 1, checked) or \
              self.helper(board, row - 1, col, word, index + 1, checked) or \
              self.helper(board, row, col - 1, word, index + 1, checked)

        checked[row][col] = False

        return res


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    sol = Solution().exist(board,word)
    print sol