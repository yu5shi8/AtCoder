# -*- coding: utf-8 -*-
# A - Best Body
# https://atcoder.jp/contests/abc022/tasks/abc022_a

n, s, t = map(int, input().split())
w = int(input())
a = [w] + [int(input()) for _ in range(n-1)]
weight = 0
best = 0

for i in range(n):
    weight += a[i]
    if s <= weight <= t:
        best += 1

print(best)

# 9:34 - 9:49
