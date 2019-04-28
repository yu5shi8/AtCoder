# -*- coding: utf-8 -*-
# B - Some Sums
# https://atcoder.jp/contests/abc083/tasks/abc083_b

n, a, b = map(int, input().split())
l = []

for i in range(1, n+1):
    num = 0
    for j in str(i):
        num += int(j)
    if a <= num <= b:
        l.append(i)

print(sum(l))

# 18:23 - 18:49
