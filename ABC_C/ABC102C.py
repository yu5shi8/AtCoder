# -*- coding: utf-8 -*-
# C - Linear Approximation
# https://atcoder.jp/contests/abc102/tasks/arc100_a

n = int(input())
a = list(map(int, input().split()))
b = [0] * n
ans = 0

for i in range(1, n+1):
    b[i-1] = a[i-1] - i

sort_b = sorted(b)
num = sort_b[n // 2]

for i in range(n):
    ans += abs(b[i] - num)

print(ans)

# 22:19 - 22:31
# 17:03 - 17:49（WA）
#（解説を閲覧）- 18:23（AC）
