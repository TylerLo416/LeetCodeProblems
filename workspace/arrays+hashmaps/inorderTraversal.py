class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        soln = []
        if root is None:
            return soln
        soln.extend(self.inorderTraversal(root.left))
        soln.append(root.val)
        soln.extend(self.inorderTraversal(root.right))
        return soln