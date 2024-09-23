
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        #Root currently points to head/parent of the TreeNode
        in_order_traversal = []
        return self.in_order_helper(root,in_order_traversal)

    def in_order_helper(self,root,in_order_traversal):
        if root.left is None:
            in_order_traversal.append(root.val)
        else:
            self.in_order_helper(root.left,in_order_traversal)
            in_order_traversal.append(root.val)

        if(root.right is not None):
            self.in_order_helper(root.right,in_order_traversal)

        return in_order_traversal





if __name__ == "__main__":
    root = None
    sol = Solution()
    print(sol.inorderTraversal(root))



