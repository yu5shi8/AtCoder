# -*- coding: utf-8 -*-
# B - Small and Large Integers
# https://atcoder.jp/contests/abc093/tasks/abc093_b

a, b, k = map(int, input().split())

for i in range(a, min(a+k, b+1)):
    print(i)
for i in range(max(a+k, b+1-k), b+1):
    print(i)

'''
for i in range(a, b+1):
    if b - k < i or i < a + k:
        print(i)
    else:
        continue
'''

# 15:32 - 15:40（TLE） - 15:58

