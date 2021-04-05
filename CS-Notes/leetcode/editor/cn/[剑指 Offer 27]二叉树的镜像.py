# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。 
# 
#  例如输入： 
# 
#  4 
#  / \ 
#  2 7 
#  / \ / \ 
# 1 3 6 9 
# 镜像输出： 
# 
#  4 
#  / \ 
#  7 2 
#  / \ / \ 
# 9 6 3 1 
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 1000 
# 
#  注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/ 
#  Related Topics 树 
#  👍 123 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(node):
            if not node: return
            node.left, node.right = node.right, node.left
            recur(node.left)
            recur(node.right)

        recur(root)
        return root
# leetcode submit region end(Prohibit modification and deletion)
