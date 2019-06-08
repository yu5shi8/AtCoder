# -*- coding: utf-8 -*-
# B - ディスプレイ
# https://atcoder.jp/contests/abc038/tasks/abc038_b

hw1 = list(map(int, input().split()))
hw2 = list(map(int, input().split()))

for i in range(2):
    if hw1[0] == hw2[i] or hw1[1] == hw2[i]:
        print('YES')
        exit()

print('NO')

# 22:25 - 22:36
