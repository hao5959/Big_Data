class Solution:
    def calPoints(self, ops):
        stack = []
        for char in ops:
            if char == 'D':
                stack.append(stack[-1] * 2)
            elif char == 'C':
                stack.pop()
            elif char == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(char))
        print(sum(stack))
res = Solution()
res.calPoints(['5', '2', 'C', 'D', '+'])