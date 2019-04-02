# -*- coding: utf-8 -*-
# A - AtCoDeerくんとペンキ
# https://atcoder.jp/contests/abc046/tasks/abc046_a

abc = list(map(int, input().split()))
count = (len(abc) + len(set(abc))) - 3
print(count)
