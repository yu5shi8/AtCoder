# -*- coding: utf-8 -*-
# C - Dice and Coin
# https://atcoder.jp/contests/abc126/tasks/abc126_c

n, k = map(int, input().split())
ans = 0

for i in range(1, n+1):
    if i >= k:
        ans += 1/n
    else:
        count = 1
        while i * 2 ** count < k:
            count += 1
        ans += (1/n) * (0.5**count)

print(ans)

# 16:44 - 16:48
