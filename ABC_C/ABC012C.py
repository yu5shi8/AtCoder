# -*- coding: utf-8 -*-
# C - 九九足し算
# https://atcoder.jp/contests/abc012/tasks/abc012_3

N = int(input())
array = [i for i in range(1, 10)]

check = 2025 - N
for i in array:
    ans = divmod(check, i)
    if ans[0] < 10 and ans[1] == 0:
        print(str(i) + ' x ' + str(ans[0]))

# 20:41 - 21:12（AC）
