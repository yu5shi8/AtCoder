# -*- coding: utf-8 -*-
# A - Cookie Exchanges
# https://atcoder.jp/contests/agc014/tasks/agc014_a

A, B, C = map(int, input().split())
a = A
b = B
c = C
count = 0

while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    count += 1
    a_pool = a // 2
    b_pool = b // 2
    c_pool = c // 2
    a = b_pool + c_pool
    b = a_pool + c_pool
    c = a_pool + b_pool
    if a == b == c:
        print(-1)
        exit()

print(count)

# 14:45 - 14:56（AC）
