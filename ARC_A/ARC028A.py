# -*- coding: utf-8 -*-
# A - 小石を取るゲーム
# https://atcoder.jp/contests/arc028/tasks/arc028_1

N, A, B = map(int, input().split())

calc = N % (A + B)

if 1 <= calc <= A:
    print('Ant')
else:
    print('Bug')

# 21:36 - 21:37（WA）- 21:39（AC）
