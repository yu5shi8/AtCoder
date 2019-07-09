# -*- coding: utf-8 -*-
# A - T or T
# https://atcoder.jp/contests/abc133/tasks/abc133_a

n, a, b = map(int, input().split())

train = n * a
taxi = b

print(min(train, taxi))

# 20:00 - 20:01（AC）
