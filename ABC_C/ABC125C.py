# -*- coding: utf-8 -*-
# C - GCD on Blackboard
# https://atcoder.jp/contests/abc125/tasks/abc125_c

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

n = int(input())
a = list(map(int, input().split()))

left = [0 for _ in range(n)]
right = [0 for _ in range(n)]
ans = [0 for _ in range(n)]

for i in range(1, n):
    left[i] = gcd(left[i-1], a[i-1])

for i in range(n-2, -1, -1):
    right[i] = gcd(right[i+1], a[i+1])

for i in range(n):
    ans[i] = gcd(left[i], right[i])

print(max(ans))

# 13:40 - 13:44
