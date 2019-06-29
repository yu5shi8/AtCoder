# -*- coding: utf-8 -*-
# C - Divide the Problems
# https://atcoder.jp/contests/abc132/tasks/abc132_c

n = int(input())
d = sorted(list(map(int, input().split())))
center = n // 2

if d[center - 1] != d[center]:
    ans = d[center] - d[center - 1]
else:
    ans = 0

print(ans)

# 21:13 - 21:27（AC）
