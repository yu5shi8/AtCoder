# -*- coding: utf-8 -*-
# A - HonestOrDishonest
# https://atcoder.jp/contests/abc056/tasks/abc056_a

ab = input().split()

if (ab.count('H') == 2) or (ab.count('D') == 2):
    print('H')
else:
    print('D')
