# 547. Friend Circles
# Difficulty: Medium
# Contributors:
# lkpunisher
# There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature.
# For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
# then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total
#  number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        num_of_student = len(M)

        checked = [0] * num_of_student
        graph = [[] for i in xrange(num_of_student)]

        for row in xrange(len(M)):
            for col in xrange(len(M[row])):
                if row != col and M[row][col]:
                    graph[row].append(col)

        print graph

        self.group = 1

        for i in xrange(num_of_student):
            self.dfs(i, graph, checked, self.group)

        return len(set(checked))

    def dfs(self, node, graph, checked, group_number):
        if checked[node] != 0:
            return

        checked[node] = group_number

        for child in graph[node]:
            self.dfs(child, graph, checked, group_number)
        self.group += 1



if __name__ == '__main__':
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print Solution().findCircleNum(M)
