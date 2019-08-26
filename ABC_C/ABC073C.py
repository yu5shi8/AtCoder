# -*- coding: utf-8 -*-
# C - Write and Erase
# https://atcoder.jp/contests/abc073/tasks/abc073_c

n = int(input())
array = {}

for i in range(n):
    a = int(input())
    if a not in array:
        array[a] = 1
    elif array[a] == 1:
        array[a] -= 1
    else:
        array[a] += 1

print(sum(array.values()))

# 15:54 - 16:01（TLE）- 16:03（WA）- 16:07（WA）- 16:12（AC）
