#-*-coding:utf-8 -*-
# 347. Top K Frequent Elements
# Difficulty: Medium
# Contributors: Admin
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
import collections
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counts = collections.Counter(nums)
        heap = []
        for key,cnt in counts.items():
            if len(heap)<k:
                heapq.heappush(heap,(cnt,key))
            else:
                if heap[0][0]< cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(cnt,key))
        return [x[1] for x in heap]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print Solution().topKFrequent(nums,2)