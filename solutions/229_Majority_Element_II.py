# 229. Majority Element II
# Difficulty: Medium
# Contributor: LeetCode
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.
#
# Hint:
#
# How many majority elements could it possibly have?
# Do you have a better hint? Suggest it!

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        a = cnt_a = cnt_b = 0
        b = 1
        for num in nums:
            if a == num:
                cnt_a += 1
            elif b == num:
                cnt_b += 1
            elif not cnt_a:
                a, cnt_a = num, 1
            elif not cnt_b:
                b, cnt_b = num, 1
            else:
                cnt_a, cnt_b = cnt_a - 1, cnt_b - 1
        return [n for n in (a, b) if nums.count(n) > len(nums) / 3]

if __name__ == '__main__':
    input = [1,1,1,2,2,1]
    print Solution().majorityElement(input)