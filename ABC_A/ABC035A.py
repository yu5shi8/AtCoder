# -*- coding: utf-8 -*-
# A - テレビ
# https://atcoder.jp/contests/abc035/tasks/abc035_a

w, h = map(int, input().split())

if w % 16 == 0 and h % 9 == 0:
    print('16:9')
else:
    print('4:3')

# 20:18 - 20:20
