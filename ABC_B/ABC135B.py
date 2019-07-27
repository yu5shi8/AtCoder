# -*- coding: utf-8 -*-
# B - 0 or 1 Swap
# https://atcoder.jp/contests/abc135/tasks/abc135_b

n = int(input())
p = list(map(int, input().split()))
count = 0

for i in range(n):
    num = i + 1
    if num != p[i]:
        count += 1

if count == 0 or count == 2:
    print('YES')
else:
    print('NO')

# 21:06 - 21:14（AC）
