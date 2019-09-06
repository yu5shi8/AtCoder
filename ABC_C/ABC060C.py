# -*- coding: utf-8 -*-
# C - Sentou
# https://atcoder.jp/contests/abc060/tasks/arc073_a

N, T = map(int, input().split())
t = list(map(int, input().split()))
X = T

for i in range(1, N):
    if t[i] - t[i-1] <= T:
        X += t[i] - t[i-1]
    else:
        X += T

print(X)

# 11:22 - 11:36（AC）
