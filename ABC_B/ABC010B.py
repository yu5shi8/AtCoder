# -*- coding: utf-8 -*-
# B - 花占い
# https://atcoder.jp/contests/abc010/tasks/abc010_2

n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(n):
    num = a[i]
    while num > 0:
        if (num - 2) % 3 == 0:
            num -= 1
            count += 1
        elif num % 2 == 0:
            count += 1
            num -= 1
        else:
            break

print(count)

# 16:07 - 16:18（AC）
