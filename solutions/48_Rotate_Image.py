# 48. Rotate Image
# Difficulty: Medium
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        matrix_len = len(matrix)
        for i in range(matrix_len):
            for j in range(matrix_len):
                if i>j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(matrix_len):
            for j in range(matrix_len/2):
                matrix[i][j],matrix[i][matrix_len-1-j] = matrix[i][matrix_len-1-j],matrix[i][j]


if __name__ == '__main__':
    img = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    Solution().rotate(img)
    for row in img:
        print row