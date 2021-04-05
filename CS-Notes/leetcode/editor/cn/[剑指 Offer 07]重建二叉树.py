# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
#  Related Topics 树 递归 
#  👍 402 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def recur(root, left, right):
            if left > right: return
            node = TreeNode(preorder[root])
            idx = dic.get(preorder[root])
            node.left = recur(root + 1, left, idx - 1)
            node.right = recur(root + idx + 1 - left, idx + 1, right)
            return node

        return recur(0, 0, len(preorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)
