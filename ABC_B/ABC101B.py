# -*- coding: utf-8 -*-
# B - Digit Sums
# https://atcoder.jp/contests/abc101/tasks/abc101_b

n = input()
n_sum = 0

for i in range(len(n)):
    n_sum += int(n[i])
if int(n) % n_sum == 0:
    print('Yes')
else:
    print('No')

# 15:41 - 15:51
