# -*- coding: utf-8 -*-
# C - Replacing Integer
# https://atcoder.jp/contests/abc161/tasks/abc161_c

N, K = map(int, input().split())
ans = N

N = N % K
n = abs(N - K)
ans = min(ans, N)
ans = min(ans, n)

print(ans)

# 17:04 - 17:23（AC）
