# -*- coding: utf-8 -*-
# A - ι⊥l
# https://atcoder.jp/contests/abc058/tasks/abc058_a

a, b, c = map(int, input().split())

if b - a == c - b:
    print('YES')
else:
    print('NO')
