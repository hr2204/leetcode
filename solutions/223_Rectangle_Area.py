# 223. Rectangle Area
# Difficulty: Easy
# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total_area = abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H)
        if C<=E or G<=A or B>=H or F>=D:
            return total_area
        x_list = [A,C,E,G]
        y_list = [D,B,H,F]
        x_list.sort()
        y_list.sort()
        x = abs(x_list[2] - x_list[1])
        y = abs(y_list[2] - y_list[1])

        return total_area - x*y




if __name__ == '__main__':
    print Solution().computeArea(0,0,0,0,-1,-1,1,1)