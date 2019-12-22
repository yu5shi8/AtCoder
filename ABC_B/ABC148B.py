# -*- coding: utf-8 -*-
# B - Strings with the Same Length
# https://atcoder.jp/contests/abc148/tasks/abc148_b

N = int(input())
S, T = map(str, input().split())
ans = ''

for i in range(N):
    ans += S[i]
    ans += T[i]

print(ans)

# 21:05 - 21:07（AC）
