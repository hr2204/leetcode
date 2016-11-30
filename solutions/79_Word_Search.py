# 79. Word Search   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 100081
# Total Submissions: 400427
# Difficulty: Medium
# Contributors: Admin
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = []
        self.flag = False
        for row in range(len(board)):
            visited.append([0]*len(board[0]))

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    self.dfs(board,word,visited,row,col,self.flag,0)
                if self.flag:
                    return True

        return False

    def dfs(self,board,word,visited,row,col,flag,word_idx):
        if self.flag:
            return


        if row<0 or col < 0 or row >=len(board) or col >= len(board[0]):
            return
        if visited[row][col]:
            return
        if board[row][col] != word[word_idx]:
            return

        if word_idx == len(word)-1:
            self.flag = True
            return



        visited[row][col] = 1
        self.dfs(board,word,visited,row,col-1,flag,word_idx+1)
        self.dfs(board,word,visited,row-1,col,flag,word_idx+1)
        self.dfs(board,word,visited,row,col+1,flag,word_idx+1)
        self.dfs(board,word,visited,row+1,col,flag,word_idx+1)

        visited[row][col] = 0

if __name__ == '__main__':
    grid = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    word_1 = "ABCCED"
    word_2 = "SEE"
    word_3 = "ABCB"
    print Solution().exist(grid,word_1)
    print Solution().exist(grid,word_2)
    print Solution().exist(grid,word_3)

    grid = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word_1 = "AAB"
    print Solution().exist(grid,word_1)


