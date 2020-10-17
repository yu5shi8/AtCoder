# -*- coding: utf-8 -*-
# B - Various distances
# https://atcoder.jp/contests/abc180/tasks/abc180_b

import math

N = int(input())
X = list(map(int, input().split()))

man = 0
eu = 0
chebi = X[0]

for x in X:
    man += abs(x)
    eu += abs(x) ** 2
    if chebi < abs(x):
        chebi = abs(x)

eu = '{:.16f}'.format(math.sqrt(eu))

print(man)
print(eu)
print(chebi)

# 20:00 - 20:07（WA）- 20:16（WA）/ 20:43 - 20:47（AC）
