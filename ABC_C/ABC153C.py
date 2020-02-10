# -*- coding: utf-8 -*-
# C - Fennec vs Monster
# https://atcoder.jp/contests/abc153/tasks/abc153_c

N, K = map(int, input().split())
H = list(map(int, input().split()))
H.sort()

if N <= K:
    ans = 0
else:
    num = N - K
    ans = sum(H[:num])

print(ans)

# 21:06 - 21:13（AC）
