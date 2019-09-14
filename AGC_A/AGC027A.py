# -*- coding: utf-8 -*-
# A - Candy Distribution Again
# https://atcoder.jp/contests/agc027/tasks/agc027_a

N, x = map(int, input().split())
a = list(map(int, input().split()))
count = 0
a.sort()

for i in range(N):
    if x == a[i]:
        count += 1
    elif i == N - 1:
        if x != a[i]:
            break
    elif x - a[i] > 0:
        x -= a[i]
        count += 1
    else:
        break

print(count)

# 6:52 - 7:10
