# -*- coding: utf-8 -*-
# C - Energy Drink Collector
# https://atcoder.jp/contests/abc121/tasks/abc121_c

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
sorted_ab = sorted(ab)

ab_price = [0] * n
num = [0] * (n+1)

for i in range(n):
    num[i+1] = num[i] + sorted_ab[i][1]
    ab_price[i] = sorted_ab[i][0] * sorted_ab[i][1]
    if num[i+1] >= m:
        to_here = i + 1
        break

max_price = sorted_ab[to_here-1][0]
minus_num = num[to_here] - m
ans = sum(ab_price[:to_here]) - max_price * minus_num

print(ans)

# 20:47 - 21:35
