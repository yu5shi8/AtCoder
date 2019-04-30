# -*- coding: utf-8 -*-
# B - Lucas Number
# https://atcoder.jp/contests/abc079/tasks/abc079_b

n = int(input())
l = [2, 1,]

if n <= 1:
    print(l[n])
else:
    for i in range(2, n+1):
        calc = l[i-2] + l[i-1]
        l.append(calc)
    print(l[n])

# 9:32 - 10:00
