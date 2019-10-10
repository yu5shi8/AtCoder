# -*- coding: utf-8 -*-
# C - 一次元リバーシ / 1D Reversi
# https://atcoder.jp/contests/abc047/tasks/arc063_a

S = list(input())
ans = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        ans += 1

print(ans)

# 14:47 - 15:43（AC）
