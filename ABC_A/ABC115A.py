# -*- coding: utf-8 -*-
# A - Christmas Eve Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_a

d = int(input())

if d == 25:
    print('Christmas')
else:
    count = 25 - d
    print('Christmas' + ' Eve' * count)
