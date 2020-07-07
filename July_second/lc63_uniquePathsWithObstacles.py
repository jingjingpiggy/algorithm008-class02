def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1:
        return 0
#    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp = [[0]*n for _ in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            if not obstacleGrid[i][j]:
                if i==j==0: # Firstly, fill in the first line and first column 
                    dp[i][j] = 1
                else:
                    # caculate the others depend the first line and first column
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[m-1][n-1]

print(uniquePathsWithObstacles([[0,0,0],[1,0,0],[0,0,0]]))
