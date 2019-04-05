# -*- coding: utf-8 -*-
# A - Two Coins
# https://atcoder.jp/contests/abc091/tasks/abc091_a

a, b, c = map(int, input().split())

if c <= a + b:
    print('Yes')
else:
    print('No')
