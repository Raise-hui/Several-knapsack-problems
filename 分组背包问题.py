'''
分别对i组物品进行枚举，再对每组物品进行枚举，（注意枚举是顺序还是倒序）
将每一种小决策的值输入dp中，小的值会被大的值所覆盖，最后的最大值就是所求。
思路：对于第i组物品来说，假设这组物品的个数为s，这组物品的最大价值递推式为。
dp[j] = max{dp[j],dp[j-v[0]]+w[0],dp[j-v[1]]+w[1],...,dp[j-v[s]]+w[s]}
有s+1种决策，即：
1.一个都不取
2.取第一个
.
.
.
s.取第s个
'''

if __name__ == '__main__':
    N, V = map(int, input().split())
    dp = [0 for _ in range(V + 1)]
    for i in range(N):
        v, w = [], []  # 枚举每组的物品前，要对v,w进行初始化
        s = int(input())
        for j in range(s):
            stuffs = (list(map(int, input().split())))
            v.append(stuffs[0])
            w.append(stuffs[1])
        for j in range(V, -1, -1):
            for k in range(s):
                if j >= v[k]:
                    dp[j] = max(dp[j], dp[j - v[k]] + w[k])
    print(dp[V])
