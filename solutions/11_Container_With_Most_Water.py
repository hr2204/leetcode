# 11. Container With Most Water
# Difficulty: Medium
# Contributors: Admin
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical
# lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
# with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# Subscribe to see which companies asked this question
#
# Show Tags
# Show Similar Problems


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        l, r = 0, len(height)-1
        while l<r:
            maxWater = max(maxWater,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return maxWater


    def maxArea_LTE(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                if (j-i)*min(height[i],height[j])>maxWater:
                    maxWater = (j-i)*min(height[i],height[j])
        return maxWater



if __name__ == '__main__':
    s = Solution()
    print Solution().maxArea([2,3,4,5,18,17,6])