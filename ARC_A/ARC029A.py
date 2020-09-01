# -*- coding: utf-8 -*-
# A - 高橋君とお肉
# https://atcoder.jp/contests/arc029/tasks/arc029_1

N = int(input())
t = [int(input()) for _ in range(N)]

total = sum(t)
temp = 500

for i in range(1, 2**N):
    a, b = 0, 0
    for j in range(N):
        if (i >> j) & 1:
            a += t[j]
            b = total - a
    check = abs(a - b)
    if check < temp:
        temp = check
        ans = max(a, b)

print(ans)

# 23:07 - 23:19（AC）
