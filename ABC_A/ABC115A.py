# -*- coding: utf-8 -*-
# A - Christmas Eve Eve Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_a

d = int(input())
count = 25

if d == 25:
    print('Christmas')
else:
    count -= d
    print('Christmas' + ' Eve' * count)

# 10:06 - 10:09 - 10:11

