# -*- coding: utf-8 -*-
# B - Choose Integers
# https://atcoder.jp/contests/abc060/tasks/abc060_b

a, b, c = map(int, input().split())

for i in range(100):
    if (a*i) % b == c:
        print('YES')
        exit()

print('NO')

# 15:01 - 15:13
