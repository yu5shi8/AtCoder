# -*- coding: utf-8 -*-
# C - management
# https://atcoder.jp/contests/abc163/tasks/abc163_c

N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

for i in A:
    ans[i-1] += 1

for j in ans:
    print(j)

# 21:57 - 22:02（AC）
