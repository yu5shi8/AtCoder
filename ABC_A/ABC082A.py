# -*- coding: utf-8 -*-
# A - Round Up the Mean
# https://atcoder.jp/contests/abc082/tasks/abc082_a

a, b = map(int, input().split())
calc = int((a + b) / 2)
check = (a + b) % 2

if check == 0:
    print(calc)
else:
    calc += 1
    print(calc)
