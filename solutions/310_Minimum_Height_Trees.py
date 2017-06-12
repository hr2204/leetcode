# -*- coding: utf-8 -*-
# 310. Minimum Height Trees
# Difficulty: Medium
# Contributor: LeetCode
# For a undirected graph with tree characteristics, we can choose any node as the root.
# The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges
# (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0]
# and thus will not appear together in edges.
#
# Example 1:
#
# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
# return [1]
#
# Example 2:
#
# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]
#
# Note:
#
# (1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
#
# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
#

class Solution(object):
    def findMinHeightTrees_LTE(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]

        node_map = [[] for i in xrange(n)]
        res = [[] for i in xrange(n)]

        for edge in edges:
            node1, node2 = edge[0], edge[1]
            if node1 not in node_map[node2]:
                node_map[node2].append(node1)
            if node2 not in node_map[node1]:
                node_map[node1].append(node2)
        print node_map

        for node in xrange(n):
            checked = [False] * n
            self.start_node = node
            self.dfs(node, node_map, res, checked, [node])
        print '='*100
        for row in res:
            print row
        print '='*100

        # print res
        res = [max([len(path) for path in row]) for row in res]
        return [node for node in xrange(n) if res[node] == min(res)]

    def dfs(self, node, node_map, res, checked, cur_list):
        if checked[node]:
            return

        checked[node] = True

        for next_node in node_map[node]:
            if len(node_map[next_node]) == 1 and not checked[next_node]:
                res[self.start_node].append(cur_list + [next_node])
            else:
                self.dfs(next_node, node_map, res, checked, cur_list+ [next_node])




if __name__ == '__main__':
    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    print Solution().findMinHeightTrees(n, edges)
