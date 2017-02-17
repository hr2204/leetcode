# 506. Relative Ranks
#
# Difficulty: Easy
# Contributors: taylorty
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
# who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
#
# Example 1:
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        order_dist = []
        for idx,num in enumerate(nums):
            order_dist.append((num,idx))
        print order_dist
        order_dist.sort(reverse=True)
        res = [0] * len(order_dist)
        for num in order_dist:
            res[num[1]] = num[0]
        print order_dist
        print res
        # print sorted(order_dist,key=order_dist.get)




if __name__ == '__main__':
    input = [5, 3, 4, 1, 2]
    print Solution().findRelativeRanks(input)