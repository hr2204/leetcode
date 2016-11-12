# 384. Shuffle an Array
# Difficulty: Medium
# Contributors: Admin
# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

import random
import copy
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.origin = copy.deepcopy(nums)
        self.new_list = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        length = len(self.new_list)
        for t in range(length):
            i = random.randint(t,length -1)
            self.new_list[i],self.new_list[t] = self.new_list[t],self.new_list[i]
        return self.new_list


if __name__ == '__main__':
    nums = ["Solution","shuffle","reset","shuffle"]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print param_1
    print param_2
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()