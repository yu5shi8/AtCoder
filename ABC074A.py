# -*- coding: utf-8 -*-
# A - Bichrome Cells
# https://atcoder.jp/contests/abc074/tasks/abc074_a

n = int(input())
a = int(input())
b = (n * n) - a

if b > 0:
    print(b)
else:
    print(0)
