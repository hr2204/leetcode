# 207. Course Schedule
# Difficulty: Medium
# Contributor: LeetCode
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should
# also have finished course 1. So it is impossible.
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
# is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering
# exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = [[] for i in xrange(numCourses)]

        # 0 : not checked
        # 1 : checked
        # -1 : being checked
        checked = [0] * numCourses

        # convert edge to graph
        for node, preNode in prerequisites:
            graph[preNode].append(node)

        print graph
        for node in xrange(numCourses):
            if self.hasCircle(node, graph, checked):
                return False

        return True

    def hasCircle(self, node, graph, checked):
        if checked[node] == -1:
            return True
        elif checked[node] == 1:
            return False

        checked[node] = -1

        for child in graph[node]:
            if self.hasCircle(child, graph, checked):
                return True

        checked[node] = 1

        return False


if __name__ == '__main__':
    numCourses, prerequisites = 2, [[1, 0]]
    print Solution().canFinish(numCourses, prerequisites)
    numCourses, prerequisites = 2, [[1, 0], [0, 1]]
    print Solution().canFinish(numCourses, prerequisites)
    numCourses, prerequisites = 3, [[0,1],[0,2],[1,2]]
    print Solution().canFinish(numCourses, prerequisites)
