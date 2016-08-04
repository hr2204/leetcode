# 220. Contains Duplicate III
# Given an array of integers, find out whether there are two distinct indices
# i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
#


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
