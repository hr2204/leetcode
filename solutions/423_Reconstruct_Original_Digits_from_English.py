# 423. Reconstruct Original Digits from English
# Difficulty: Medium
# Contributors: Admin
# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
#
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# Example 2:
# Input: "fviefuro"
#
# Output: "45"
import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        letters = collections.Counter(s)
        res = ""
        num_list = [0] * 10
        print letters
        # count zero by 'z'
        num_list[0] = letters['z']
        letters['e'] -= letters['z']
        letters['r'] -= letters['z']
        letters['o'] -= letters['z']

        #count two by 'w'
        num_list[2] = letters['w']
        letters['t'] -= letters['w']
        letters['r'] -= letters['w']
        letters['o'] -= letters['w']

        #count four by 'u'
        num_list[4] = letters['u']
        letters['f'] -= letters['u']
        letters['r'] -= letters['u']
        letters['o'] -= letters['u']

        #count four by 'x'
        num_list[6] = letters['x']
        letters['s'] -= letters['x']
        letters['i'] -= letters['x']

        #count four by 'g'
        num_list[8] = letters['g']
        letters['e'] -= letters['g']
        letters['i'] -= letters['g']
        letters['h'] -= letters['g']
        letters['t'] -= letters['g']

        #count one by 'o'
        num_list[1] = letters['o']

        #count three by 'h'
        num_list[3] = letters['h']

        #count three by 'f'
        num_list[5] = letters['f']
        letters['i'] -= letters['f']

        #count seven by 's'
        num_list[7] = letters['s']

        #count nine by 'i'
        num_list[9] = letters['i']

        for idx,num in enumerate(num_list):
            res += str(idx)*num
        return res
if __name__ == '__main__':
    input_1 = "owoztneoer"
    input_2 = "fviefuro"

    print Solution().originalDigits(input_1)
    print Solution().originalDigits(input_2)