# -*- coding: utf-8 -*-
# B - トリボナッチ数列
# https://atcoder.jp/contests/abc006/tasks/abc006_2

n = int(input())
array = [0, 0, 1]

for i in range(2, n):
    a = array[i - 1]
    b = array[i - 2]
    c = array[i]
    num = a + b + c
    num %= 10007
    array.append(num)

print(array[n - 1])

# 19:45 - 19:55（TLE）- 20:02（解説AC）
