# -*- coding: utf-8 -*-
# A - 勝率計算
# https://atcoder.jp/contests/abc030/tasks/abc030_a

a, b, c, d = map(int, input().split())

if b/a == d/c:
    print('DRAW')
elif b/a > d/c:
    print('TAKAHASHI')
else:
    print('AOKI')

# 21:48 - 21:51
