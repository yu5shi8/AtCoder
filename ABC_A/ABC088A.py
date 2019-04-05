# -*- coding: utf-8 -*-
# A - Infinite Coins
# https://atcoder.jp/contests/abc088/tasks/abc088_a

n = int(input())
a = int(input())

ans = n % 500

if ans <= a:
    print('Yes')
else:
    print('No')
