# -*- coding: utf-8 -*-
# A - Expired?
# https://atcoder.jp/contests/abc065/tasks/abc065_a

x, a, b = map(int, input().split())

if x + a < b:
    print('dangerous')
elif a >= b:
    print('delicious')
else:
    print('safe')
