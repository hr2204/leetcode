# 383. Ransom Note  QuestionEditorial
# Difficulty: Easy
#  Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,
# write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;
#   otherwise,  it  will  return  false.   
#
# Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        charDict = dict()
        for char in magazine:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1
        for char in ransomNote:
            if char in charDict and charDict[char] > 0:
                charDict[char] -= 1
            else:
                return False
        return True



if __name__ == '__main__':
    print Solution().canConstruct("a","b")
    print Solution().canConstruct("aa", "ab")
    print Solution().canConstruct("aa", "aab")