# -*- coding: utf-8 -*-
# B - Minor Change
# https://atcoder.jp/contests/abc172/tasks/abc172_b

S = input()
T = input()
n = len(S)
ans = 0

for i in range(n):
    if S[i] != T[i]:
        ans += 1

print(ans)

# 21:01 - 21:02（AC）
