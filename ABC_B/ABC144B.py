# -*- coding: utf-8 -*-
# B - 81
# https://atcoder.jp/contests/abc144/tasks/abc144_b

N = int(input())
ans = []

for i in range(1, 10):
    for j in range(1, 10):
        ans.append(i*j)

if N in ans:
    print('Yes')
else:
    print('No')

# 21:02 - 21:05（AC）
