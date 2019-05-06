# -*- coding: utf-8 -*-
# B - Trained?
# https://atcoder.jp/contests/abc065/tasks/abc065_b

n = int(input())
a = [int(input()) for i in range(n)]
l = [0]*n
num = 0

for i in a:
    l[num] += 1
    if l[1] == 1:
        print(sum(l)-1)
        break
    else:
        num = a[num]-1
        if l[num] == 2:
            print(-1)
            exit()

# 22:59 - 24:21
