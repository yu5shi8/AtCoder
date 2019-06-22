# -*- coding: utf-8 -*-
# D - Megalomania
# https://atcoder.jp/contests/abc131/tasks/abc131_d

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort(key=lambda x:x[1])

cost = 0
limit = 0

for i in range(n):
    cost += ab[i][0]
    limit = ab[i][1]
    if limit < cost:
        print('No')
        exit()

print('Yes')

# 22:29 - 22:40（WA）- 22:59（AC）
