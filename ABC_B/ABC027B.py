# -*- coding: utf-8 -*-
# B - 島と橋
# https://atcoder.jp/contests/abc027/tasks/abc027_b

n = int(input())
a = list(map(int, input().split()))

num = 0
p = sum(a) // n
ans = 0

if sum(a) % n != 0:
    print(-1)
    exit()

for i in range(1, n):
    if a[i - 1] < p:
        num = p - a[i - 1]
        a[i - 1] = p
        a[i] -= num
        ans += 1
    elif a[i - 1] > p:
        num = a[i - 1] - p
        a[i - 1] = p
        a[i] += num
        ans += 1

print(ans)

# 19:42 - 20:50
# 21:33 - 21:41（AC）
