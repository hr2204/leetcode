# 319. Bulb Switcher  QuestionEditorial Solution  My Submissions
# Total Accepted: 28794
# Total Submissions: 69389
# Difficulty: Medium
# There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb.
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
# For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# Find how many bulbs are on after n rounds.
#
# Example:
#
# Given n = 3.
#
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off].
#
# So you should return 1, because there is only one bulb is on.
import math
class Solution(object):
    def bulbSwitch(self,n):

        return math.floor(math.sqrt(n))
    # LTE
    def bulbSwitch_LTE(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [False] * n
        # print bulbs
        for i in range(n):
            for j in range(i,n):
                if (j+1)%(i+1)==0:
                    bulbs[j] = not bulbs[j]
            print bulbs
        res = 0
        for bulb in bulbs:
            if bulb == True:
                res += 1
        return res
if __name__ == '__main__':
    print Solution().bulbSwitch(1) == 1
    print Solution().bulbSwitch(2) == 1
    print Solution().bulbSwitch(3) == 1
    print Solution().bulbSwitch(4) == 2
    print Solution().bulbSwitch(5) == 2
    print Solution().bulbSwitch(6) == 2