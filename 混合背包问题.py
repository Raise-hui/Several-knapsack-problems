if __name__ == '__main__':
    N, V = map(int, input().split())
    dp = [0 for _ in range(V + 1)]
    things = []
    for i in range(N):
        stuffs = list(map(int, input().split()))
        v = stuffs[0]
        w = stuffs[1]
        s = stuffs[2]
        if s < 0:
            things.append([-1, v, w])
        elif s == 0:
            things.append([0, v, w])
        else:
            k = 1
            while k <= s:
                things.append([-1, k * v, k * w])
                s -= k
                k *= 2
            if s:
                things.append([-1, s * v, s * w])
    for block in things:
        v = block[1]
        w = block[2]
        if block[0] == -1:
            for j in range(V, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + w)
        elif block[0] == 0:
            for j in range(v, V + 1):
                dp[j] = max(dp[j], dp[j - v] + w)
    print(dp[V])
