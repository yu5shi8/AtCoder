# -*- coding: utf-8 -*-
# A - AtCoder Crackers
# https://atcoder.jp/contests/abc105/tasks/abc105_a

n, k = map(int, input().split())

if n % k != 0:
    print(1)
else:
    print(0)
