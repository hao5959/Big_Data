class Solution:
    def largestValues(self, root):
        
        if not root: return []
        res = []
        queue = [root]
        
        while queue:
            max_val = float('-inf')
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)
                max_val = max(max_val, node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max_val)
        return res