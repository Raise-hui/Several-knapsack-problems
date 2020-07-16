'''
dp[j]:背包内物品的体积恰好是j的最大价值是dp[j]
g[j]:背包内物体的体积恰好是j且取得最大价值时的方案数
决策1:如果体积为j时取得最大价值时不需要放当前物品，则 s += g[j];
决策2:如果体积为j时取得最大价值时需要放置当前物品，则 s += g[j-v]
最后g[j] = s

先算一下选不选当前物品的两种决策的最大价值时多少，再看一下到底从哪一个
决策转移过来。如果两种决策的最大价值不一样，那么就从大的决策那里取出方案数。
如果两种决策的最大价值一样，那么就需要把两种决策的方案数相加。

最后，根据初始化的原因，最终最大价值不一定在dp[j]处取得，因此我们需要遍历一遍dp数组，求出最大价值。
然后根据最大价值，找到此时对应的总方案数g[j]，把所有等于最大价值的总方案数累加起来即可。另外记得取模
'''

if __name__ == '__main__':
    mod = 10 ** 9 + 7
    N, V = map(int, input().split())
    dp = [float('-inf') for _ in range(V + 1)]
    dp[0] = 0  # 初始化为负无穷,只有dp[0]有0值
    g = [0 for _ in range(V + 1)]
    g[0] = 1  # g[0]表示体积为0时的方案数，初始化为1，只有一种方案，全都不装
    for i in range(N):
        v, w = map(int, input().split())
        for j in range(V, v - 1, -1):  # 逆序遍历体积
            s = 0
            t = max(dp[j], dp[j - v] + w)  # 不为负无穷的前提就是存在若干个物品的体积恰好为j-v，或者j==v
            if t == dp[j]:
                s += g[j]
            if t == dp[j - v] + w:
                s += g[j - v]
            s = s % mod if s >= mod else s
            dp[j] = t
            g[j] = s
    # 计算取得最大价值时的总方案数
    # 先找出最大价值
    max_v = 0
    for i in range(len(dp)):
        max_v = max(max_v, dp[i])
    # 再找出最大价值的方案数
    res = 0
    for i in range(len(g)):
        if dp[i] == max_v:
            res += g[i]
        res = res % mod if res >= mod else res
    print(res)
