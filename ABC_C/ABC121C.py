# -*- coding: utf-8 -*-
# C - Energy Drink Collector
# https://atcoder.jp/contests/abc121/tasks/abc121_c

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab_l = sorted(ab)
ans = 0

count = [0]*(n+1)
for i in range(n):
    count[i+1] = count[i] + ab_l[i][1]

for i in range(n+1):
    if count[i] >= m:
        to_here = i
        minus_count = count[to_here] - m
        break

all_money = [0]*n
for i in range(to_here):
    all_money[i] = ab_l[i][0] * ab_l[i][1]

ans = sum(all_money) - ab_l[to_here-1][0] * minus_count

print(ans)

# 21:14 - 22:41
# 23:20 - 23:56