# -*- coding: utf-8 -*-
# C - Next Prime
# https://atcoder.jp/contests/abc149/tasks/abc149_c

import math

def is_prime(n):
    if n == 2:
        return True

    for k in range(2, int(math.sqrt(n)) + 1):
        if X % k == 0:
            return False
    return True

X = int(input())

while 2 <= X <= 100010:
    if is_prime(X) == True:
        print(X)
        break
    X += 1

# 20:10 - 20:25（AC）
