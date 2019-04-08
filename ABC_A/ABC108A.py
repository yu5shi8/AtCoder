# -*- coding: utf-8 -*-
# A - Pair
# https://atcoder.jp/contests/abc108/tasks/abc108_a

k = int(input())
ans = 0

if k % 2 == 0:
    ans = (k // 2) * (k // 2)
else:
    ans = (k // 2) * (k // 2 + 1)

print(ans)