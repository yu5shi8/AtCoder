# -*- coding: utf-8 -*-
# A - Parking
# https://atcoder.jp/contests/abc080/tasks/abc080_a

n, a, b = map(int, input().split())

a_fee = a * n
b_fee = b

if a_fee < b_fee:
    print(a_fee)
else:
    print(b_fee)
