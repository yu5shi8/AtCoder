# -*- coding: utf-8 -*-
# A - Move and Win
# https://atcoder.jp/contests/agc020/tasks/agc020_a

n, a, b = map(int, input().split())

if n == b and abs(a - b) == 1:
    print('Borys')
elif abs(a - b) % 2 == 0:
    print('Alice')
elif abs(a - b) % 2 != 0:
    print('Borys')
else:
    print('Draw')

# 10:33 - 10:57（AC）
