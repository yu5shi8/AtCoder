# -*- coding: utf-8 -*-
# A - Between Two Integers
# https://atcoder.jp/contests/abc061/tasks/abc061_a

a, b, c = map(int, input().split())

if c >= a and c <= b:
    print('Yes')
else:
    print('No')
