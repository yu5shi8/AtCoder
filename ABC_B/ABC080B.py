# -*- coding: utf-8 -*-
# B - Harshad Number
# https://atcoder.jp/contests/abc080/tasks/abc080_b

n = int(input())
num = sum(map(int, list(str(n))))

if n % num == 0:
    print('Yes')
else:
    print('No')

# 16:55 - 17:32（答えを見た）
