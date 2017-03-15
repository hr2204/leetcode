# 150. Evaluate Reverse Polish Notation
# Difficulty: Medium
# Contributors: Admin
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = set(['+','-','*','/'])
        # if len(tokens) == 1:
        #     return tokens[0]
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                self.calculate_token(stack,token)
        return stack[-1]

    def calculate_token(self,stack,operator):
        num1 = stack.pop()
        num2 = stack.pop()
        if operator == '+':
            res = int(num1) + int(num2)
        elif operator == '-':
            res = int(num2) - int(num1)
        elif operator == '*':
            res = int(num1) * int(num2)
        else:
            res = int(float(num2) / float(num1))
        stack.append(res)
        print res
        return res


if __name__ == '__main__':
    # input_1 = ["2", "1", "+", "3", "*"]
    # input_2 = ["4", "13", "5", "/", "+"]
    input_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # print Solution().evalRPN(input_2)
    print Solution().evalRPN(input_3)
