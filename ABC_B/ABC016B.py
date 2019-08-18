# -*- coding: utf-8 -*-
# B - A±B Problem
# https://atcoder.jp/contests/abc016/tasks/abc016_2

a, b, c = map(int, input().split())

if a + b == c and a - b == c:
    print('?')
elif a + b == c and a - b != c:
    print('+')
elif a + b != c and a - b == c:
    print('-')
else:
    print('!')

# 10:01 - 10:04（AC）
