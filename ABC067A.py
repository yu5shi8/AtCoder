# -*- coding: utf-8 -*-
# A - Sharing Cookies
# https://atcoder.jp/contests/abc067/tasks/abc067_a

a, b = map(int, input().split())
c = (a + b)

if a % 3 == 0 or b % 3 == 0:
    print('Possible')
elif c % 3 == 0:
    print('Possible')
else:
    print('Impossible')
