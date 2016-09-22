# 228. Summary Ranges
# Difficulty: Medium
# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res
        idx = 0
        while idx < len(nums):
            start, end = nums[idx],nums[idx]
            for i in range(idx+1,len(nums)):
                if nums[i] == nums[i-1]+1:
                    end = nums[i]
                else:
                    break
                idx = i+1
            if start!=end:
                res.append(str(start)+"->"+str(end))
            else:
                res.append(str(start))
                idx += 1
        return res

if __name__ == '__main__':
    print Solution().summaryRanges([0,1])