# -*- coding: utf-8 -*-
# A - 暗証番号
# https://atcoder.jp/contests/abc033/tasks/abc033_a

n = input()

if n.count(n[0]) == 4:
    print('SAME')
else:
    print('DIFFERENT')

# 21:27 - 21:36
