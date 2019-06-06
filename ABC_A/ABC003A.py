# -*- coding: utf-8 -*-
# A - AtCoder社の給料
# https://atcoder.jp/contests/abc003/tasks/abc003_1

n = int(input())
num = 0

for i in range(1, n+1):
    num += 10000 * i

print(num / n)

# 11:12 - 11:15

