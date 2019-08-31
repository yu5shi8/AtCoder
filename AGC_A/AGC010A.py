# -*- coding: utf-8 -*-
# A - Addition
# https://atcoder.jp/contests/agc010/tasks/agc010_a

N = int(input())
A = list(map(int, input().split()))
odd = 0
even = 0

for a in A:
    if a % 2 != 0:
        odd += 1
    else:
        even += 1

if odd % 2 == 0:
    print('YES')
else:
    print('NO')

# 18:03 - 18:16（WA） - 18:20（AC）
