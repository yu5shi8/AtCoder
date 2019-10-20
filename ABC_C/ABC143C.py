# -*- coding: utf-8 -*-
# C - Slimes
# https://atcoder.jp/contests/abc143/tasks/abc143_c

N = int(input())
S = input()
ans = 1

for i in range(1, N):
    if S[i-1] != S[i]:
        ans += 1

print(ans)

# 21:09 - 21:11（AC）
