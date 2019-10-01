# -*- coding: utf-8 -*-
# C - X: Yet Another Die Game
# https://atcoder.jp/contests/abc053/tasks/arc068_a

x = int(input())
count = 0

if x <= 6:
    count = 1
else:
    a, b = divmod(x, 11)
    a *= 2
    if b == 0:
        a += 0
    elif b > 6:
        a += 2
    else:
        a += 1
    count = a

print(count)

# 13:07 - 13:34（AC）
