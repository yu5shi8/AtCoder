# -*- coding: utf-8 -*-
# C - Walk on Multiplication Table
# https://atcoder.jp/contests/abc144/tasks/abc144_c

N = int(input())
ans = []

for i in range(1, int(pow(N, 0.5))+1):
    if N % i == 0:
        j = N // i
        ans.append(i-1+j-1)

print(min(ans))

# 21:02 - 21:30（WA）- 22:45（AC）
