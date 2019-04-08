# -*- coding: utf-8 -*-
# A - ABC333
# https://atcoder.jp/contests/abc109/tasks/abc109_a

a, b = map(int, input().split())

if a != 2 and b != 2:
    print('Yes')
else:
    print('No')

# a * b が偶数にならないよう条件分けするとスマート
