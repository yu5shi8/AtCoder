# -*- coding: utf-8 -*-
# A - Digit Sum 2
# https://atcoder.jp/contests/agc021/tasks/agc021_a

N = list(input())
num_1 = 0
num_2 = 0

for i in range(len(N)):
    if i == 0:
        num_1 += int(N[i]) - 1
    else:
        num_1 += 9

for n in N:
    num_2 += int(n)

print(max(num_1, num_2))

# 18:23 - 18:56（WA）- 19:01（AC）
