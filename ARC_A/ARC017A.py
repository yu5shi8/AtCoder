# -*- coding: utf-8 -*-
# A - 素数、コンテスト、素数
# https://atcoder.jp/contests/arc017/tasks/arc017_1

N = int(input())

for i in range(2, N):
    if N % i == 0:
        print('NO')
        exit()

print('YES')

# 17:44 - 17:47（AC）
