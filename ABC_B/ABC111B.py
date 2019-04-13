# -*- coding: utf-8 -*-
# B - AtCoder Beginner Contest 111
# https://atcoder.jp/contests/abc111/tasks/abc111_b

n = int(input())
num = 111

while num <= 999:
    if n <= num:
        print(num)
        break
    else:
        num += 111
