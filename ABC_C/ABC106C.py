# -*- coding: utf-8 -*-
# C - To Infinity
# https://atcoder.jp/contests/abc106/tasks/abc106_c

s = input()
k = int(input())
count = 0

for i in range(k):
    if s[i] == '1':
        count += 1
        if count == k:
            print(1)
    else:
        print(s[i])
        exit()

# 15:38 - 16:16（AC）
