# 299. Bulls and Cows
# Difficulty: Easy
# You are playing the following Bulls and Cows game with your friend: You write down a number and
#  ask your friend to guess what the number is. Each time your friend makes a guess, you provide a
# hint that indicates how many digits in said guess match your secret number exactly in both digit
# and position (called "bulls") and how many digits match the secret number but locate in the
#  wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.
#
# For example:
#
# Secret number:  "1807"
# Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and friend's guess, use A to indicate
# the bulls and B to indicate the cows. In the above example, your function should return "1A3B".
#
# Please note that both secret number and friend's guess may contain duplicate digits, for example:
#
# Secret number:  "1123"
# Friend's guess: "0111"
# In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
# You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

import collections, operator

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = sum(map(operator.eq, secret, guess))
        sa = collections.Counter(secret)
        sb = collections.Counter(guess)
        cow = sum((sa & sb).values()) - bull
        return str(bull) + 'A' + str(cow) + 'B'

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = sum(map(operator.eq, secret, guess))
        sa = collections.Counter(secret)
        sb = collections.Counter(guess)
        cow = sum((sa & sb).values()) - bull
        return str(bull) + 'A' + str(cow) + 'B'

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        numDict = dict()
        numDict1 = dict()
        a, b = 0, 0
        secret = list(secret)
        guess = list(guess)

        i = 0
        while i <len(secret):
            if secret[i] == guess[i]:
                a += 1
                secret.pop(i)
                guess.pop(i)
            else:
                if secret[i] not in numDict:
                    numDict[secret[i]] = 1
                else:
                    numDict[secret[i]] += 1

                if guess[i] not in numDict1:
                    numDict1[guess[i]] = 1
                else:
                    numDict1[guess[i]] += 1
                i += 1
        for digit in numDict:
            if digit in numDict1:
                b += min(numDict[digit],numDict1[digit])

        return str(a) + "A" + str(b )+ "B"

if __name__ == "__main__":
    print  Solution().getHint("1122","2211")
    assert Solution().getHint("1807","7810") == "1A3B"