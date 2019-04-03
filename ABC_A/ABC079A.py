# -*- coding: utf-8 -*-
# A - Good Integer
# https://atcoder.jp/contests/abc079/tasks/abc079_a

n = input()

if n[0] == n[1] and n[0] == n[2]:
    print('Yes')
elif n[3] == n[1] and n[3] == n[2]:
    print('Yes')
else:
    print('No')

