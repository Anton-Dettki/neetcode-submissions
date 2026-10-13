class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            print(stack)
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif len(stack) != 0 and c == stack[-1]:
                stack.pop()
            else:
                return False
        if not bool(stack):
            return True
        else:
            return False
        