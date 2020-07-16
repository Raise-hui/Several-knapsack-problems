N, V, M = map(int, input().split())
dp = [[0 for i in range(M + 1)] for j in range(V + 1)]
stuffs = []
for i in range(N):
    stuffs.append(list(map(int, input().split())))
for i in range(len(stuffs)):
    v = stuffs[i][0]
    m = stuffs[i][1]
    w = stuffs[i][2]
    for j in range(V, v - 1, -1):
        for k in range(M, m - 1, -1):
            dp[j][k] = max(dp[j][k], dp[j - v][k - m] + w)
print(dp[V][M])
