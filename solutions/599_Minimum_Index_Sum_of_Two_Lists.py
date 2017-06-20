# 599. Minimum Index Sum of Two Lists
# Difficulty: Easy
# Contributors:
# love_Fawn
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.
#
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        map1 = self.convet_to_map(list1)
        map2 = self.convet_to_map(list2)
        res = []
        max_idx_sum = len(list1) + len(list2)
        for key in map1:
            if key in map2:
                if map1[key] + map2[key] < max_idx_sum:
                    res = [key]
                    max_idx_sum = map1[key] + map2[key]
                elif map1[key] + map2[key] == max_idx_sum:
                    res.append(key)
        return res

    def convet_to_map(self,list):
        list_map = {}
        for i in xrange(len(list)):
            list_map[list[i]] = i
        return list_map


if __name__ == '__main__':
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    print Solution().findRestaurant(list1,list2)
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print Solution().findRestaurant(list1,list2)
