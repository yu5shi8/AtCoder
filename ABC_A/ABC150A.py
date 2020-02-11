# -*- coding: utf-8 -*-
# A - 500 Yen Coins
# https://atcoder.jp/contests/abc150/tasks/abc150_a

K, X = map(int, input().split())

calc = 500 * K
if calc >= X:
    print('Yes')
else:
    print('No')

# 22:35 - 2:37（AC）
