# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
# it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
#  are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution(object):
        def trap(self, height):
            """
            :type height: List[int]
            :rtype: int
            """

            ans = 0
            max_left = list(height)
            max_right = list(height)

            for i in range(1,len(height)):
                if max_left[i] < max_left[i-1]:
                    max_left[i] = max_left[i-1]

            for i in range(0,len(height)-1)[::-1]:
                if max_right[i] < max_right[i+1]:
                    max_right[i] = max_right[i+1]

            for i in range(1,len(height)-1):
                left_max = max_left[i-1]
                right_max = max_right[i+1]


                if min(left_max, right_max) > height[i]:
                    ans += min(left_max, right_max) - height[i]

            return ans


    def LTE_trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0

        for i in range(1, len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])

            if min(left_max, right_max) > height[i]:
                ans += min(left_max, right_max) - height[i]

        return ans

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    print sol.trap(height)

# Output: 6