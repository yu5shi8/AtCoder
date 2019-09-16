# -*- coding: utf-8 -*-
# C - Attack Survival
# https://atcoder.jp/contests/abc141/tasks/abc141_c

N, K, Q = map(int, input().split())
ans = ['No'] * N
s_array = [K] * N
c_array = [0] * N

for i in range(Q):
    A = int(input())
    c_array[A-1] += 1

sum_array = sum(c_array)

for i in range(N):
    calc = s_array[i] + c_array[i] - sum_array
    if calc > 0:
        ans[i] = 'Yes'

print(*ans, sep='\n')

# 16:15 - 16:51（AC）
