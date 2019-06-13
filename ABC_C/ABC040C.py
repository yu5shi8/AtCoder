# -*- coding: utf-8 -*-
# C - 柱柱柱柱柱
# https://atcoder.jp/contests/abc040/tasks/abc040_c

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[1] = abs(a[1] - a[0])

for i in range(2, n):
    dp[i] = min(dp[i-1]+abs(a[i]-a[i-1]), dp[i-2]+abs(a[i]-a[i-2]))

print(dp[-1])

# 18:12 - 18:24
