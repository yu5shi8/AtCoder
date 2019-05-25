# -*- coding: utf-8 -*-
# C - Prison
# https://atcoder.jp/contests/abc127/tasks/abc127_c

n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]
left = []
right = []

for i in range(m):
    left.append(lr[i][0])
    right.append(lr[i][1])

ans = min(right) - max(left) + 1

if ans < 0:
    ans = 0

print(ans)

# 21:23 - 22:11（wA）
# 22:17（AC）
