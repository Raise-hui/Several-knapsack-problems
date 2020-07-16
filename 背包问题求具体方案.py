'''
1、由于题目要求求字典序最小的方案，因此从1到n中，每个物品有3种情况
(1)只能选，则必须选
(2)不能选，则必不选
(3)可选可不选，则必须选
在前面物品能选的情况下优先选择前面的物品
2、为了满足上述条件，因此需要从第n个物品遍历到第1个物品，求出当前背包的最大总价值f[1][m]
3、再从第1个物品遍历到第n个物品，其中f[i][j]为当前最优情况，若满足
(1)f[i][j] == f[i + 1][j],则表示f[i][j]是从f[i + 1][j]状态转移过来的
(2)f[i][j] == f[i + 1][j - v[i]] + w[i]，则表示f[i][j]是从f[i + 1][j - v[i]]状态转移过来的
从而找出字典序最小的路径方案
代码编写思路：
f[1][V]一定是最大价值，那么f[1][V]怎么求呢？
f[i,j]定义为从第i个元素到最后一个元素总容量为j的最优解。接下来考虑状态转移
f[i,j]=max(f[i+1,j],f[i+1,j−v[i]]+w[i]]
那么f[N][0]的值一定是最小值0，因此我们以这个状态开始状态转移。
即N -> 1 ; 0 -> V ，求解f[N][0] -> f[1][V]
'''

if __name__ == '__main__':
    N, V = map(int, input().split())
    dp = [[0 for _ in range(V + 2)] for _ in range(N + 2)]
    v, w = [0], [0]
    for i in range(N):
        stuffs = list(map(int, input().split()))
        v.append(stuffs[0])
        w.append(stuffs[1])
    # 求最大价值
    for i in range(N, -1, -1):
        for j in range(V + 1):
            dp[i][j] = dp[i + 1][j]
            if j >= v[i]:
                dp[i][j] = max(dp[i + 1][j - v[i]] + w[i], dp[i][j])
    print(dp)
    # 求最小字典序
    vol = V
    for i in range(1, N + 1):
        if (dp[i][vol] == dp[i + 1][vol - v[i]] + w[i]) and v[i] <= vol:  # 如果选取第i个物品才是最优解
            print(i, end=' ')
            vol -= v[i]
