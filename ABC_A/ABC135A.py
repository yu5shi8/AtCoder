# -*- coding: utf-8 -*-
# A - Harmony
# https://atcoder.jp/contests/abc135/tasks/abc135_a

a, b = map(int, input().split())

if (a + b) % 2  == 0:
    print((a + b) // 2)
else:
    print('IMPOSSIBLE')

# 21:00 - 21:05（AC）
