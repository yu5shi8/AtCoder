# -*- coding: utf-8 -*-
# A - B +/- A
# https://atcoder.jp/contests/abc118/tasks/abc118_a

a, b = map(int, input().split())

if b % a == 0:
    print(a+b)
else:
    print(b-a)


# 22:15 - 22:17
