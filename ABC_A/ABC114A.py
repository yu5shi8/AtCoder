# -*- coding: utf-8 -*-
# A - 753
# https://atcoder.jp/contests/abc114/tasks/abc114_a

x = int(input())
if x == 7 or x == 5 or x == 3:
    print('YES')
else:
    print('NO')

# スマートに書く方法がある
# if x in [7, 5, 3]:
