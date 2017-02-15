# 500. Keyboard Row
#
# Difficulty: Easy
# Contributors: Admin
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard
# like the image below.
#
#
# American keyboard
#
#
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = ["q","w","e",'r',"t",'y','u','i','o','p']
        second_row = ['a','s','d','f','g','h','j','k','l']
        third_row = ['z','x','c','v','b','n','m']
        tmp = []
        for word in words:
            if word[0].lower() in first_row:
                for char in word:
                    if char.lower() not in first_row:
                        tmp.append(word)
                        break
            elif word[0].lower() in second_row:
                for char in word:
                    if char.lower() not in second_row:
                        tmp.append(word)
                        break
            else:
                for char in word:
                    if char.lower() not in third_row:
                        tmp.append(word)
                        break

        res=[]
        for word in words:
            if word not in tmp:
                res.append(word)
        return res



        return words
if __name__ == '__main__':
    print Solution().findWords(["asdfghjkl", "Alaska", "Dad", "Peace"])