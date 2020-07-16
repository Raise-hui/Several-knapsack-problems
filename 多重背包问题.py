'''
n:物品的种数
m:背包的容量
vi:第i个物品的体积
wi:第i个物品的价值
si:第i个物品的数量
'''

'''
朴素法

class Solution(object):
    def max_value(self, n, m, v, w, s):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for k in s:
                for j in range(m, k * v[i] - 1, -1):
                    dp[j] = max(dp[j], dp[j - k * v[i]] + k * w[i])
        return dp[m]
        
if __name__ == '__main__':
    n, m = map(int, input().split())
    v, w, s = [0], [0], [0]
    for i in range(n):
        line = list(map(int, input().split()))
        v.append(line[0])
        w.append(line[1])
        s.append(line[2])
    print(Solution().max_value(n, m, v, w, s))
'''

'''
二进制优化法
多重背包问题转换成（0 - 1背包问题）
N:代表物品的种类
m:背包的容积
n:二分化后物品的份数
vi:第i份物品的体积
wi:第i份物品的价值
'''


class Solution(object):
    def max_value(self, n, m, v, w):
        dp = [0 for _ in range(m + 1)]
        for i in range(n):
            for j in range(m, v[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        return dp[m]


if __name__ == '__main__':
    N, m = map(int, input().split())
    v, w = [], []
    n = 0
    for i in range(N):
        k = 1
        line = list(map(int, input().split()))
        while k <= line[2]:
            v.append(k * line[0])
            w.append(k * line[1])
            line[2] -= k
            k *= 2
            n += 1
        if line[2]:
            v.append(line[2] * line[0])
            w.append(line[2] * line[1])
            n += 1

    print(Solution().max_value(n, m, v, w))
