# -*- coding: utf-8 -*-
# C - Many Medians
# https://atcoder.jp/contests/abc094/tasks/arc095_a

n = int(input())
x = list(map(int, input().split()))
y = sorted(x[:])

for i in range(n):
    if x[i] < y[n//2]:
        print(y[n//2])
    else:
        print(y[n//2 - 1])

# 18:02 - 18:28（TLE）
#（解説を閲覧）- 21:47
