# 253. Meeting Rooms II
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        temp = []
        for interval in intervals:
            temp.append((interval.start, True))
            temp.append((interval.end, False))
        # temp.sort(key=lambda x:x[0])
        # [(1, True), (13, True), (13, False), (15, False)]

        temp.sort(key=lambda v: (v[0], v[1]))

        print temp
        cnt, max_cnt = 0, 0
        for interval in temp:
            if (interval[1]):
                cnt += 1
            else:
                cnt -= 1
            max_cnt = max(cnt, max_cnt)

        return max_cnt
