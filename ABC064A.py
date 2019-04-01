# -*- coding: utf-8 -*-
# A - RGB Cards
# https://atcoder.jp/contests/abc064/tasks/abc064_a

r, g, b = input().split()
i = r + g + b
if int(i) % 4 == 0:
    print('YES')
else:
    print('NO')
