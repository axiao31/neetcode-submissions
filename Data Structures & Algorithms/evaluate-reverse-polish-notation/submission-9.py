class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = tokens[0]
        stack=[]
        for c in tokens:
            if c not in ['+', '-', '*', '/']:
                stack.append(int(c))
            elif c == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n1 + n2
                stack.append(res)
            elif c == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 - n1
                stack.append(res)
            elif c == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(n2 / n1)
                stack.append(res)
            elif c == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                res = n1 * n2
                stack.append(res)
            print(stack)
        return stack.pop()