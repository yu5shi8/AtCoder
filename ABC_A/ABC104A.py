# -*- coding: utf-8 -*-
# A - Rated for Me
# https://atcoder.jp/contests/abc104/tasks/abc104_a

r = int(input())
if r < 1200:
    print('ABC')
elif r >= 1200 and r < 2800:
    print('ARC')
else:
    print('AGC')
