# 128. Longest Consecutive Sequence
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        checked = {num: False for num in nums}
        num_dict = set(nums)
        res = 0
        for num in nums:
            if not checked[num]:
                checked[num] = True
                left = 0
                cur = num - 1

                while cur in num_dict:
                    checked[cur] = True
                    left += 1
                    cur -= 1

                right = 0
                cur = num + 1

                while cur in num_dict:
                    checked[cur] = True
                    right += 1
                    cur += 1

            res = max(res, 1 + left + right)

        return res

if __name__ == '__main__':
    input = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print sol.longestConsecutive(input)