# -*- coding: utf-8 -*-
# A - Add Sub Mul
# https://atcoder.jp/contests/abc098/tasks/abc098_a

a, b = map(int, input().split())

add = a + b
sub = a - b
multi = a * b

print(max(add, sub, multi))
