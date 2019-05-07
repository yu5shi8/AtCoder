# -*- coding: utf-8 -*-
# B - Counting Roads
# https://atcoder.jp/contests/abc061/tasks/abc061_b

n, m = map(int, input().split())
ans = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    ans[a-1] += 1
    ans[b-1] += 1

for i in ans:
    print(i)

# 14:30 - 14:52
