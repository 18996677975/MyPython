# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 
#  👍 220 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return matrix

        r1, r2, c1, c2 = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        res = []
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                res.append(matrix[r1][i])
            for i in range(r1 + 1, r2 + 1):
                res.append(matrix[i][c2])
            if r1 != r2:
                for i in range(c2 - 1, r1 - 1, -1):
                    res.append(matrix[r2][i])
            if c1 != c2:
                for i in range(r2 - 1, c1, -1):
                    res.append(matrix[i][c1])

            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return res
# leetcode submit region end(Prohibit modification and deletion)
