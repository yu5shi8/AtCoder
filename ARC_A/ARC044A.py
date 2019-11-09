# -*- coding: utf-8 -*-
# A - 素数判定
# https://atcoder.jp/contests/arc044/tasks/arc044_a

import math

N = int(input())

if N == 1:
    print('Not Prime')
    exit()

def is_prime(n):
    for k in range(2, int(math.sqrt(n))+1):
        if n % k == 0:
            return False
    return True

if is_prime(N):
    print('Prime')
else:
    n = str(N)
    l = []
    for i in n:
        l.append(int(i))
    num = 0
    if l[-1] in [1, 3, 7, 9]:
        for i in l:
            num += i
        if num % 3 != 0:
            print('Prime')
        else:
            print('Not Prime')
    else:
        print('Not Prime')

# 14:33 - 15:03（AC）
