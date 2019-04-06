# -*- coding: utf-8 -*-
# A - Cats and Dogs
# https://atcoder.jp/contests/abc094/tasks/abc094_a

a, b, x = map(int, input().split())

if x < a:
    print('NO')
elif b > x - a:
    print('YES')
else:
    print('NO')
