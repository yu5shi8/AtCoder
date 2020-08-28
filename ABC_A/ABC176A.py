# -*- coding: utf-8 -*-
# A - Takoyaki
# https://atcoder.jp/contests/abc176/tasks/abc176_a

N, X, T = map(int, input().split())

time = divmod(N, X)
ans = 0

if time[1] != 0:
    ans = T * (time[0] + 1)
else:
    ans = T * time[0]

print(ans)

# 18:02 - 18:07（AC）
