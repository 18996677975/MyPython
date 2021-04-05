# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
#  Related Topics 回溯算法 
#  👍 239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        def dfs(x):
            if x == len(c) - 1:
                res.append(''.join(c))      # 添加排序方式
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic: continue    # 重复，剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]
                dfs(x+1)
                c[i], c[x] = c[x], c[i]

        dfs(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
