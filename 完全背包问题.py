'''
if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = [0 for _ in range(m + 1)]
    v, w = [0], [0]
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        v.append(line[0])
        w.append(line[1])
        for j in range(v[i], m + 1):
            dp[j] = max(dp[j], dp[j - v[i]] + w[i])
    print(dp[m])
'''
if __name__ == '__main__':
    n, m = map(int, input().split())
    stuffs = []
    dp = [0 for _ in range(m + 1)]
    for i in range(n):
        stuffs.append(list(map(int, input().split())))
    for i in range(len(stuffs)):
        v = stuffs[i][0]
        w = stuffs[i][1]
        for j in range(v, m + 1):
            dp[j] = max(dp[j], dp[j - v] + w)
    print(dp[m])
