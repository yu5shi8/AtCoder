# -*- coding: utf-8 -*-
# B - Around Square
# https://atcoder.jp/contests/abc077/tasks/abc077_b

n = int(input())
for i in range(n, 0, -1):
    calc = pow(i, 0.5)
    if calc.is_integer():
        break
print(i)

# 10:36 - 10:45
