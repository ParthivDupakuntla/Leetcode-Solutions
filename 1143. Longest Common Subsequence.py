class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        #dp1 = [[0]*(n+1)]*(m+1)
        #print(dp1)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j]  = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[m-1][n-1]
        
        
        
