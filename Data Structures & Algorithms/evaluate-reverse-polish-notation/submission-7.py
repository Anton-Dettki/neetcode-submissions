class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                f = stack.pop()
                s = stack.pop()
                if c == "+":
                    stack.append(int(f+s))
                if c == "-":
                    stack.append(int(s-f))
                if c == "*":
                    stack.append(int(f*s))
                if c == "/":
                    stack.append(int(s/f))
        return stack.pop()
        


        

    # tokens= 1, 3, +, 4, -

    #s = []
    # 1
    # 3, 1
    # f= s.pop sec = s.pop
    # s = []
    # compute f SIGN sec
    # s.push(result)
    # 4
    # 4, 4
