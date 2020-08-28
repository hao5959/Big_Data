class TreeNode:
    def __init__(self, left, right, data):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    def constructMaximumBinaryTree(self, nums):
        stack = []
        for num in nums:
            node = TreeNode(num)
            while len(stack) > 0 and stack[-1].val < num:
                node.left = stack.pop()
            if len(stack) > 0:
                stack[-1].right = node
            stack.append(node)
            
        return stack[0]