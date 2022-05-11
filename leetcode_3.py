### Regular Expression Matching

### solution 1 (recursion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursion(i, j):
            if j == len(p):
                if i == len(s):
                    return True
                return False
            if j + 1 < len(p):
                if p[j + 1] == '*':
                    tmp = recursion(i, j + 2)
                    if i < len(s):
                        if s[i] == p[j] or p[j] == '.':
                            tmp = tmp or recursion(i + 1, j)
                    return tmp 
            if i < len(s):
                if s[i] == p[j] or p[j] == '.':
                    return recursion(i + 1, j + 1)
            return False

        return recursion(0, 0)
      
### soulution 2 (DP)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = True

        for i in range(m):
            if p[i] == '*':
                dp[0][i+1] = dp[0][i-1]
        for j in range(1,n+1):
            for i in range(1,m+1):
                if p[i-1] == s[j-1] or p[i-1] == '.':
                    dp[j][i] = dp[j-1][i-1]
                elif p[i-1] == '*':
                    dp[j][i] = dp[j][i-2]
                    if p[i-2] == '.' or p[i-2] == s[j-1]:
                        dp[j][i] = dp[j][i] or dp[j-1][i]
        return dp[n][m]
