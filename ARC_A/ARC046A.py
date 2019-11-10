# -*- coding: utf-8 -*-
# A - ゾロ目数
# https://atcoder.jp/contests/arc046/tasks/arc046_a

zorome = []
for i in range(1, 555556):
    check = str(i)
    if check.count(check[-1]) == len(check):
        zorome.append(i)

N = int(input()) - 1
print(zorome[N])

# 17:56 - 18:03（AC）
