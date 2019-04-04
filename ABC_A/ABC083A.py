# -*- coding: utf-8 -*-
# A - Libra
# https://atcoder.jp/contests/abc083/tasks/abc083_a

a, b, c, d = map(int, input().split())
l = a + b
r = c + d

if r < l:
    print('Left')
elif r > l:
    print('Right')
else:
    print('Balanced')
