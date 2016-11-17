# 341. Flatten Nested List Iterator
# Difficulty: Medium
# Contributors: Admin
# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
# Given the list [[1,1],2,[1,1]],
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
#
# Example 2:
# Given the list [1,[4,[6]]],
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
#

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = []
        self.helper(nestedList,self.nestedList)
        self.idx = 0

    def helper(self,list,res):
        for elem in list:
            if elem.isInteger():
                res.append(elem.getInteger())
            else:
                self.helper(elem.getList(),res)


    def next(self):
        """
        :rtype: int
        """
        res = self.nestedList[self.idx]
        self.idx += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.nestedList)


# Your NestedIterator object will be instantiated and called as such:
if __name__ == '__main__':
    # test case 1
    nestedList = [[1,1],2,[1,1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print v

    # test case 2
    nestedList = [1,[4,[6]]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
    print v