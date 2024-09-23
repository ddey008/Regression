class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        return self.recursion(root, targetSum,0, [])[0]

    def recursion(self, root, targetSum,sum, list, counter = 0, hasReached = False):
        if root is None:
            return list, hasReached
        sign = -1 if root.val < 1 else 1
        sum += root.val
        if targetSum == sum and root.left is None and root.right is None:
            list[counter].insert(0,root.val)
            hasReached = True

        # Going down the left nodes/branches
        if root.left is not None:
            self.recursion(root.left, targetSum, sum,list)
        # Going down the right nodes/branches
        if root.right is not None:
            self.recursion(root.right, targetSum, sum,list)
        sum -= sign*root.val
        return list, hasReached


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))
