# -*- coding: utf-8 -*-
# A - Restricted
# https://atcoder.jp/contests/abc063/tasks/abc063_a

ab = list(map(int, input().split()))

if sum(ab) >= 1 and sum(ab) <= 9:
    print(sum(ab))
else:
    print('error')
