# -*- coding: utf-8 -*-
# C - いっしょ / Be Together
# https://atcoder.jp/contests/abc043/tasks/arc059_a

N = int(input())
a = list(map(int, input().split()))
cost_odd = 0
cost_even = 0

if a.count(a[0]) == N:
    print(0)
    exit()

num_even = sum(a) // N + 1
num_odd = sum(a) // N

for i in range(N):
    cost_even += (a[i] - num_even)**2
    cost_odd +=  (a[i] - num_odd)**2

print(min(cost_odd, cost_even))

# 14:36 - 15:20（AC）
