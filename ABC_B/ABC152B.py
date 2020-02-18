# -*- coding: utf-8 -*-
# B - Comparing Strings
# https://atcoder.jp/contests/abc152/tasks/abc152_b

a, b = map(int, input().split())

if a <= b:
    print(str(a) * b)
else:
    print(str(b) * a)

# 23:32 - 23:36（AC）
