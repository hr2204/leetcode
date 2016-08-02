# 54. Spiral Matrix
# Difficulty: Medium
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


def spiralOrder(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    res = []
    x = 0
    y = 0
    left = 0
    top = 0
    right = len(matrix[0])
    bot = len(matrix)
    while left<right and top < bot:
        for x in range(left,right):
            res.append(matrix[top][x])
        top += 1
        for y in range(top,bot):
            res.append(matrix[y][right-1])
        right -=1
        if bot<=top: break

        for x in range(left,right)[::-1]:
            res.append(matrix[bot-1][x])
        bot -= 1
        if right<left: break
        for y in range(top,bot)[::-1]:
            res.append(matrix[y][left])
        left += 1

    # if len(matrix)%2!=0 and len(matrix[0])%2!=0:
    #     res.append(matrix[len(matrix)/2][len(matrix[0])/2])

    return res

matrix2 = [[1,2]]
matrix = [[1,2],[3,4]]
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]

print spiralOrder(matrix1)
