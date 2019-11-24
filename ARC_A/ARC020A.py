# -*- coding: utf-8 -*-
# A - 石を滑らせるゲーム
# https://atcoder.jp/contests/arc020/tasks/arc020_1

A, B = map(int, input().split())

A = abs(0 - A)
B = abs(0 - B)

if A < B:
    print('Ant')
elif A > B:
    print('Bug')
else:
    print('Draw')

# 19:00 - 19:02（AC）
