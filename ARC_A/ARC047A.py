# -*- coding: utf-8 -*-
# A - タブの開きすぎ
# https://atcoder.jp/contests/arc047/tasks/arc047_a

N, L = map(int, input().split())
S = input()
num = 1
crash = 0

for i in range(N):
    if S[i] == '+':
        num += 1
    else:
        num -= 1
    if num > L:
        crash += 1
        num = 1

print(crash)

# 10:28 - 10:32（AC）
