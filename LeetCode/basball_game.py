class Solution:
    def calPoints(self, ops):
        
        total = 0
        stack = []
        
        for i in ops:
            if i.isdigit() or i.startswith('-'):
                stack.append(int(i))
                total += int(i)
            elif i == '+' and stack:
                t = stack[-1] + stack[-2]
                total += t
                stack.append(t)
            elif i == 'C':
                v = stack.pop()
                total -= v
            else:
                total += stack[-1] * 2
                stack.append(stack[-1] * 2)
                
        return total