# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def size(node):
            if not node:
                return 0
            else:
                return 1 + size(node.left) + size(node.right) 
        
        if not root:
            return 0
        
        sizeOfLeftSubtree = size(root.left)
        if k <= sizeOfLeftSubtree:
            return self.kthSmallest(root.left, k)
        elif k == sizeOfLeftSubtree + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - sizeOfLeftSubtree - 1)


            
        