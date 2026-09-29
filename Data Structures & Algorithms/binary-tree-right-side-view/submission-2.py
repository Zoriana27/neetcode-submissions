# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightNodes = []
        if not root:
            return rightNodes
        q = deque()
        levels = []
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                popped_node = q.popleft();
                if popped_node:
                    level.append(popped_node.val)
                    q.append(popped_node.left)
                    q.append(popped_node.right)
            if level:
                levels.append(level)
        for level in levels:
            if len(level) > 1:
                rightNodes.append(level[-1])
            else:
                rightNodes.append(level[0])
        return rightNodes
            

        
        