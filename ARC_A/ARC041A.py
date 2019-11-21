# -*- coding: utf-8 -*-
# A - コインの反転
# https://atcoder.jp/contests/arc041/tasks/arc041_a

x, y = map(int, input().split())
k = int(input())

if k <= y:
    ans = x + k
else:
    ans = x + y - (k - y)

print(ans)

# 10:34 - 10:39（AC）
