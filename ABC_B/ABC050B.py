# -*- coding: utf-8 -*-
# B - Contest with Drinks Easy
# https://atcoder.jp/contests/abc050/tasks/abc050_b

n = int(input())
t = list(map(int, input().split()))
m = int(input())
px = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    l = t[:]
    num = int(px[i][0]-1)
    l[num] = px[i][1]
    print(sum(l))

# 23:20 - 23:54
