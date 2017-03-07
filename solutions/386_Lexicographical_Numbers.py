# 386. Lexicographical Numbers
# Difficulty: Medium
# Contributors: Admin
# Given an integer n, return 1 - n in lexicographical order.
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
# Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
#
# Subscribe to see which companies asked this question.


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1,10):
            if i>n:
                break
            else:
                res.append(i)
                self.dfs(i,n,res)

        return res

    def dfs(self,i,n,res):
        for j in range(0,10):
            temp = i * 10 + j
            if temp > n:
                break
            else:
                res.append(temp)
                self.dfs(temp,n,res)


if __name__ == '__main__':
    temp = Solution().lexicalOrder(123)
    print len(temp) , temp