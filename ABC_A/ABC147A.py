# -*- coding: utf-8 -*-
# A - Blackjack
# https://atcoder.jp/contests/abc147/tasks/abc147_a

A1, A2, A3 = map(int, input().split())

if (A1 + A2 + A3) >= 22:
    print('bust')
else:
    print('win')

# 21:00 - 21:01（AC）
