# -*- coding: utf-8 -*-
# C - Maximal Value
# https://atcoder.jp/contests/abc140/tasks/abc140_c

N = int(input())
B = list(map(int, input().split()))
A = [B[0]] + [0]*(N-2) + [B[-1]]

for i in range(1, N-1):
    A[i] = min(B[i-1], B[i])

print(sum(A))

# [1] 21:12 - 22:04（WA）時間切れ - 22:53（AC）
# [2] 23:14 - 23:21（AC）
