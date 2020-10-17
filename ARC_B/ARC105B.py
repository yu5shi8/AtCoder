# -*- coding: utf-8 -*-
# B - MAX-=min
# https://atcoder.jp/contests/arc105/tasks/arc105_b

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = int(input())
a = list(map(int, input().split()))

num = min(a)
L = make_divisors(num)

for i in range(N):
    for l in L:
        if a[i] % l != 0:
            L.remove(l)

print(max(L))

# 22:43 - 23:27（TLE）- 23:35（TLE）- 23:47（TLE）- 0:01（AC）
