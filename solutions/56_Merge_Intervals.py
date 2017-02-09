# 56. Merge Intervals
#
# Difficulty: Medium
# Contributors: Admin
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key=lambda x:x.start)
        res = []
        for interval in intervals:
            if len(res)==0 or interval.start>res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(interval.end,res[-1].end)
        return res
if __name__ == '__main__':
    Intervals = []
    interval_2 = Interval(2,6)
    interval_1 = Interval(1,3)
    Intervals.append(interval_1)
    Intervals.append(interval_2)

    print Solution().merge(Intervals)