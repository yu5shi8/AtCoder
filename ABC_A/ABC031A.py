# -*- coding: utf-8 -*-
# A - ゲーム
# https://atcoder.jp/contests/abc031/tasks/abc031_a

a, d = map(int, input().split())
a_plus = (a+1) * d
d_plus = a * (d+1)
print(max(a_plus, d_plus))

# 21:44 - 21:47
