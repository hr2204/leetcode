# 17. Letter Combinations of a Phone Number
# Difficulty: Medium
# Contributors: Admin
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
#
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        num_dict = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"],
                    }
        res = num_dict[digits[0]]
        for i in range(1,len(digits)):
            res = self.helper(res,num_dict[digits[i]])
        return res

    def helper(self,res,chars):
        output = []

        for orign in res:
            for char in chars:
                output.append(orign + char)
        return output

if __name__ == '__main__':
    print Solution().letterCombinations("243")
    # assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
