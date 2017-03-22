# 216. Combination Sum III
# Difficulty: Medium
# Contributors: Admin
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
# and each combination should be a unique set of numbers.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def search(start,cnt,sum,nums):
            if cnt>k or sum > n:
                return
            if cnt == k and sum == n:
                res.append(nums)
                return
            for i in xrange(start+1,10):
                search(i,cnt+1,sum+i,nums+[i])
        search(0,0,0,[])

        return res


if __name__ == '__main__':
    print Solution().combinationSum3(3,9)