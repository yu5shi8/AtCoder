# -*- coding: utf-8 -*-
# A - Meal Delivery
# https://atcoder.jp/contests/abc071/tasks/abc071_a

x, a, b = map(int, input().split())
a = abs(x - a)
b = abs(x - b)

if a < b:
    print('A')
else:
    print('B')
