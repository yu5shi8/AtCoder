# -*- coding: utf-8 -*-
# A - Range Product
# https://atcoder.jp/contests/agc002/tasks/agc002_a

a, b = map(int, input().split())
num = abs(b - a + 1)

if a <= 0 <= b:
    print('Zero')
elif a < 0 and b < 0:
    if num % 2 == 0:
        print('Positive')
    else:
        print('Negative')
else:
    print('Positive')

# 9:57 - 10:12（AC）
