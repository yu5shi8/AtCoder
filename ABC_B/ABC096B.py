# -*- coding: utf-8 -*-
# B - Maximum Sum
# https://atcoder.jp/contests/abc096/tasks/abc096_b

a, b, c = map(int, input().split())
k = int(input())

for i in range(k):
    if a >= b >= c:
        a *= 2
    elif b >= c:
        b *= 2
    else:
        c *= 2

print(a + b + c)

# 15:08 - 15:18
