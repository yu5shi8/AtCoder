# -*- coding: utf-8 -*-
# A - Multiple of 2 and N
# https://atcoder.jp/contests/abc102/tasks/abc102_a

n = int(input())

if n % n == 0 and n % 2 == 0:
    print(n)
else:
    print(n * 2)

# n % n == 0 の条件式は記載不要でした
