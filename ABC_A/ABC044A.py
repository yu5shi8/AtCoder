# -*- coding: utf-8 -*-
# A - 高橋君とホテルイージー
# https://atcoder.jp/contests/abc044/tasks/abc044_a

n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n > k:
    fee = (k * x) + ((n - k) * y)
else:
    fee = n * x

print(fee)
