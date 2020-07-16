'''
二维DP解法
if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    v, w = [0], [0]
    for i in range(n):
        line = list(map(int, input().split()))
        v.append(line[0])
        w.append(line[1])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if j > v[i]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + w[i])
    for i in range(n):
        res = dp[i][j]
    print(res)
'''

# 优化之后，一维DP
'''
f[j]:体积小于等于j时的最大价值

'''
n, m = map(int, input().split())
dp = [0 for _ in range(m + 1)]
stuffs = []
for i in range(n):
    stuffs.append(list(map(int, input().split())))
for i in range(len(stuffs)):
    v = stuffs[i][0]
    w = stuffs[i][1]
    for j in range(m, v - 1, -1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(dp[m])
