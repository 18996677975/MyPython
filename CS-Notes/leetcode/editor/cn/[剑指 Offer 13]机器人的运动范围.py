# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：m = 2, n = 3, k = 1
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：m = 3, n = 1, k = 0
# 输出：1
#  
# 
#  提示： 
# 
#  
#  1 <= n,m <= 100 
#  0 <= k <= 20 
#  
#  👍 261 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def digitSum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        res = 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                if digitSum(i) + digitSum(j) <= k and (dp[i][j-1] or dp[i-1][j]):
                    res += 1
                    dp[i][j] = True

        return res
# leetcode submit region end(Prohibit modification and deletion)
