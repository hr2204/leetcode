# 54 Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res

        top, bot, left, right = 0, len(matrix), 0, len(matrix[0])

        while left < right and top < bot:
            for idx in range(left, right):
                res.append(matrix[top][idx])

            top += 1

            for idx in range(top, bot):
                res.append(matrix[idx][right-1])

            right -= 1

            if top >= bot:
                break

            for idx in range(left, right)[::-1]:
                res.append(matrix[bot-1][idx])

            bot -= 1

            if left >= right:
                break

            for idx in range(top, bot)[::-1]:
                res.append(matrix[idx][left])

            left += 1

        return res

if __name__ == '__main__':
    matrix = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]

    matrix = [[2,3]]
    print(Solution().spiralOrder(matrix))