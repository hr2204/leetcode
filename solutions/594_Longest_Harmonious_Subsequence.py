# 594. Longest Harmonious Subsequence
# Difficulty: Easy
# Contributors:
# love_Fawn
# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        res = 0
        keys = map.keys()
        keys.sort()

        for i in range(len(keys)-1):
            if abs(keys[i] - keys[i+1]) == 1:
                temp = map[keys[i]] + map[keys[i+1]]
                if temp > res:
                    res = temp
        return res




if __name__ == '__main__':
    input = [1,3,2,2,5,2,3,7]
    input = [68,66,48,61,-90,89,87,50,42,-58,80,38,77,39,64,76,9,-56,86,-46,38,23,62,55,92,46,56,95,-60,94,-44,14,23,97,35,79,55,16,97,2,-29,19,-27,66,32,68,15,39,-55,22,33,-18,78,-16,10,89,91,24,-70,-30,-40,-42,65,55,0,-78,96,35,99,62,38,1,31,63,72,-53,-30,64,-93,54,95,78,70,94,18,73,18,-55,10,52,79,99,-23]
    print Solution().findLHS(input)