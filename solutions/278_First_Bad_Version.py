# 278. First Bad Version
# Difficulty: Easy
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all
#  the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
# find the first bad version. You should minimize the number of calls to the API.
#


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        if isBadVersion(1):
            return 1

        while start <= end :
            mid = (start + end)/2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:
                    end = mid
            else:
                start = mid + 1



def isBadVersion(n):
    return [False,True][n-1]

if __name__ == '__main__':
    print Solution().firstBadVersion(2)